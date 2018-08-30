import glob
import os
import pandas as pd
import sys

from tools.analizer import normalize

sys._enablelegacywindowsfsencoding()

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, '*.csv')

def getVkData(force_reload = True):
    pickle_path = os.path.join(current_dir, 'vk.pkl')
    pickle_exist = os.path.isfile(pickle_path)

    if not force_reload and pickle_exist:
        return pd.read_pickle(pickle_path)
    else:
        if pickle_exist:
            os.remove(pickle_path)

        vkDataFrame = pd.concat([pd.read_csv(f, index_col=0, encoding='utf-8') for f in glob.glob(path)],
                                ignore_index=True).dropna(how='any')

        vkDataFrame['normalized_text'] = vkDataFrame['text'].apply(lambda text: ' '.join(normalize(text)))
        vkDataFrame.to_pickle(pickle_path)

        return vkDataFrame

