from typing import List
import glob
import os
import pandas as pd
import sys
from emoji import UNICODE_EMOJI

from tools.normalizer import normalize
from tools.stop_words import strip_stopwords

# sys._enablelegacywindowsfsencoding()

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, '*.csv')


def get_normal_tokens(tokens_parsed=[]):
    return [t[0] for t in tokens_parsed]

def fetch_emojis(text: str) -> List:
    return [char for char in text if char in UNICODE_EMOJI]

def getCaramelData(force_reload = False) -> pd.DataFrame:
    pickle_path = os.path.join(current_dir, 'vk_caramel.pkl')
    pickle_exist = os.path.isfile(pickle_path)

    if not force_reload and pickle_exist:
        return pd.read_pickle(pickle_path)
    else:
        if pickle_exist:
            os.remove(pickle_path)

        vkDataFrame = pd.concat([pd.read_csv(f, encoding='utf-8') for f in glob.glob(path)],
                                ignore_index=True).dropna(subset=['text'])

        vkDataFrame['parsed_tokens'] = vkDataFrame['text'].apply(lambda text: normalize(text))

        vkDataFrame['normal_tokens'] = vkDataFrame['parsed_tokens'].apply(get_normal_tokens)
        vkDataFrame['normal_tokens_as_string'] = vkDataFrame['normal_tokens'].apply(lambda tokens: ' '.join(tokens))

        vkDataFrame['emoji'] = vkDataFrame['parsed_tokens'] = vkDataFrame['text'].apply(fetch_emojis)

        vkDataFrame.to_pickle(pickle_path)

        return vkDataFrame

