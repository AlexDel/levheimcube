import os
from glob import glob
from functools import reduce

import pandas as pd

from misc.constants import RANDOM_STATE


def prepare_dataset(folder_path: str, field_name: str = 'text', limit=None) -> None:
    csv_mask = '*.csv'
    full_path = os.path.join(folder_path, csv_mask)
    csv_files = glob(full_path)

    federated_texts = reduce(
        lambda text_acc, text_from_path: [*text_acc, *text_from_path],
        map(lambda path: csv_filepath_to_shuffled_list(path, field_name, limit), csv_files)
    )



    df = pd.DataFrame({f'INPUT:{field_name}': federated_texts}).sample(frac=1).reset_index(drop=True)
    df.to_csv('federated.tsv', sep='\t', index=False)


def csv_filepath_to_shuffled_list(path, field_name, limit):
    df = pd.read_csv(path)

    return df[field_name].sample(n=limit, random_state=RANDOM_STATE).values


prepare_dataset('/home/developer/Загрузки/ds', field_name='text', limit=496)
