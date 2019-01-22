from misc.enums import CubeEmotionClass
from misc.types import tags_emotions_mapping

from data.vk_api_data_scraper import fetch_results_by_emotion_mapping

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

results = fetch_results_by_emotion_mapping(-34215577, overhear_mapping, '')

for emotion in CubeEmotionClass:
    results[results['emotion'] == emotion.value].to_csv(emotion.value + '_overhear_' + '.csv', encoding='utf-8')
