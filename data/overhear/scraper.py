import os

from misc.enums import CubeEmotionClass
from misc.types import tags_emotions_mapping

from data.vk_api_data_scraper import VkAPIDataScraper

overhear_public = {
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
    (CubeEmotionClass.DISGUST, ['#Подслушано_фууу@overhear'])
]

scraper = VkAPIDataScraper(overhear_public, overhear_mapping, '12476b1412476b1412476b14cb1226b4871124712476b1448e911b2216dd87466073f19')
scraper.fetch_results_by_emotion_mapping()
scraper.export_to_csv(os.getcwd())

