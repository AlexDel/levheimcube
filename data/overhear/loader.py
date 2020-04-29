import glob
import os
import pandas as pd
import sys

from tools.normalizer import normalize, not_normalize
from tools.stop_words import strip_stopwords

# sys._enablelegacywindowsfsencoding()

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, '*.csv')


def get_normal_tokens(tokens_parsed=[]):
    return [t[0] for t in tokens_parsed]


def get_vk_data(force_reload = False) -> pd.DataFrame:
    pickle_path = os.path.join(current_dir, 'vk.pkl')
    pickle_exist = os.path.isfile(pickle_path)

    if not force_reload and pickle_exist:
        return pd.read_pickle(pickle_path)
    else:
        if pickle_exist:
            os.remove(pickle_path)

        vkDataFrame = pd.concat([pd.read_csv(f, encoding='utf-8') for f in glob.glob(path)],
                                ignore_index=True).dropna(how='any')

        vkDataFrame['punctuation_tokens'] = vkDataFrame['text'].apply(lambda text: not_normalize(text))

        vkDataFrame['parsed_tokens'] = vkDataFrame['text'].apply(lambda text: normalize(text))

        vkDataFrame['normal_tokens'] = vkDataFrame['parsed_tokens'].apply(get_normal_tokens)
        vkDataFrame['normal_tokens_as_string'] = vkDataFrame['normal_tokens'].apply(lambda tokens: ' '.join(tokens))

        vkDataFrame.to_pickle(pickle_path)

        return vkDataFrame

