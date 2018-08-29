import glob
import os
import pandas as pd
import sys

sys._enablelegacywindowsfsencoding()

currentDir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(currentDir, '*.csv')

def getVkData(force_reload = True):
    picklePath = os.path.join(currentDir, 'vk.pkl')
    pickleExist = os.path.isfile(picklePath)

    if not pickleExist or not force_reload:
        dataframe = pd.concat([pd.read_csv(f, index_col=0, encoding='utf-8') for f in glob.glob(path)], ignore_index = True).dropna(how='any')
        dataframe.to_pickle(picklePath)

        return dataframe

    return pd.read_pickle(picklePath)

