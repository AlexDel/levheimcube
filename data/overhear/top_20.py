from data.overhear import getVkData
from tools.most_informative_features import get_n_most_informative_features

data = getVkData()

get_n_most_informative_features(data.to_dict('records'))
