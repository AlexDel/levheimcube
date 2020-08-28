import json

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


MONOAMINES_KEYS = ['ser', 'dop', 'nor']


def make_dataframe_from_raw_url(file_url: str, csv_path: str = None) -> pd.DataFrame:
    """
    Converts inital raw data from Toloka annotated files to DF with monoaming coords.

    :return pd.DataFrame:
    """
    df = pd.read_csv(file_url, sep='\t')

    for index, row in df.iterrows():
        df.loc[index, 'text'] = row['INPUT:text']
        df.loc[index, 'text_measure'] = row['INPUT:text']
        coords = calc_vector_coords_from_data(row)
        for mono_amine_key in MONOAMINES_KEYS:
            df.loc[index, mono_amine_key] = coords[mono_amine_key]

    # Rescale to period [-1,1] with 0 as center.
    for mono_amine_key in MONOAMINES_KEYS:
        df[mono_amine_key] =  MinMaxScaler().fit_transform(df[mono_amine_key].values.reshape(-1, 1))
    
    if csv_path is not None:
        df.to_csv(csv_path)

    return df

def calc_vector_coords_from_data(row) -> dict:
    """
    Convertrs raw estimation to vector coords
    """
    # Coords are kept in format (x,y, z) where x - ser, y - nor, z- dop
    mapped_directions_vecs = {
        'shame_excitement': [1, 1, 1],
        'disgust_rage': [-1, 1, 1],
        'fear_surprise': [1, 1, -1],
        'enjoyment_distress': [-1, 1, -1]
    }
    survey_values = json.loads(row['text_measure'])

    result_vec = np.zeros(3)
    for key in survey_values.keys():
        # Shift starting point from center to cube's 0 and calc point.
        diag_vec = (np.array(mapped_directions_vecs[key]) * survey_values[key]) + 5
        result_vec = result_vec + diag_vec

    result_vec = result_vec / 4

    return dict(ser=result_vec[0], nor=result_vec[1], dop=result_vec[2])


def select_outlier_data_by_monoamine_percentile(df: pd.DataFrame, percentile: float = 0.1) -> None:
    """
    This function allows to get texts that correspond to "extreme" monoamines values. Extremeness is defined in
    terms of percentile. Saves results in csv
    """
    if percentile <= 0:
        raise Exception('Percentile cannot be less then zero')

    if percentile > 1:
        raise Exception('Percentile cannot be greater than one')

    lower_border = 0 + percentile
    upper_border = 1 - percentile

    for key in MONOAMINES_KEYS:
        lower_value = df[key].quantile(lower_border)
        upper_value = df[key].quantile(upper_border)

        high_level_texts = df[df[key] > upper_value]['text']
        low_level_texts = df[df[key] < lower_value]['text']

        for level, texts in zip(('high', 'low'), (high_level_texts, low_level_texts)):
            filename = f'{level}_{key}.csv'
            texts.to_csv(filename)

if __name__ == '__main__':
    # Put your custom processing logic here (But don't commit)
    pass
