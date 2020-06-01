from data.overhear import get_vk_data
from tools.most_informative_features import get_n_most_informative_features

data = get_vk_data()

get_n_most_informative_features(data.to_dict('records'))
