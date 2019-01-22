import pandas as pd

from misc.enums import CubeEmotionClass
from misc.types import tags_emotions_mapping, vk_group

from data.vk_api_data_scraper import fetch_results_by_emotion_mapping

overhear_public: vk_group = {
    'id': -34215577,
    'slug': 'overhear'
}

overhear_mapping: tags_emotions_mapping = [
    (CubeEmotionClass.ANGER, ['#Подслушано_БЕСИТ@overhear']),
    (CubeEmotionClass.EXCITEMENT, ['#Подслушано_успех@overhear']),
    (CubeEmotionClass.DISTRESS, ['#Подслушано_одиночество@overhear']),
    (CubeEmotionClass.STARTLE, ['#Подслушано_странное@overhear']),
    (CubeEmotionClass.FEAR, ['#Подслушано_страшное@overhear']),
    (CubeEmotionClass.ENJOYMENT, ['#Подслушано_счастье@overhear']),
    (CubeEmotionClass.SHAME, ['#Подслушано_стыдно@overhear']),
    (CubeEmotionClass.DISGUST, ['#Подслушано_фууу@overhear']),
]


results = fetch_results_by_emotion_mapping(overhear_public, overhear_mapping, '12476b1412476b1412476b14cb1226b4871124712476b1448e911b2216dd87466073f19')
resultsDF = pd.DataFrame(results)

for emotion in CubeEmotionClass:
    resultsDF[resultsDF['emotion'] == emotion.value].to_csv(f'{emotion.value}_{overhear_public["name"]}.csv', encoding='utf-8')
