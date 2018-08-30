import glob
import os
import pandas as pd
import sys

from tools.analizer import normalize

sys._enablelegacywindowsfsencoding()

currentDir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(currentDir, '*.csv')

def getVkData(force_reload = True):
    picklePath = os.path.join(currentDir, 'vk.pkl')
    pickleExist = os.path.isfile(picklePath)

    if not force_reload and pickleExist:
        return pd.read_pickle(picklePath)
    else:
        if pickleExist:
            os.remove(picklePath)

        vkDataFrame = pd.concat([pd.read_csv(f, index_col=0, encoding='utf-8') for f in glob.glob(path)],
                                ignore_index=True).dropna(how='any')

        vkDataFrame['normalized_text'] = vkDataFrame['text'].apply(normalize)
        vkDataFrame.to_pickle(picklePath)

        return vkDataFrame

