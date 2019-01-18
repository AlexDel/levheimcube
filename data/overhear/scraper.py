import re
from time import sleep

import pandas as pd
import vk

from misc.enums import CubeEmotionClass
from misc.types import tagsEmotionsMapping

session = vk.Session(access_token='')
vk_api = vk.API(session)

tagsEmotionsMapping: tagsEmotionsMapping = [
    (CubeEmotionClass.ANGER, ['#Подслушано_БЕСИТ@overhear']),
    (CubeEmotionClass.EXCITEMENT, ['#Подслушано_успех@overhear']),
    (CubeEmotionClass.DISTRESS, ['#Подслушано_одиночество@overhear']),
    (CubeEmotionClass.STARTLE, ['#Подслушано_странное@overhear']),
    (CubeEmotionClass.FEAR, ['#Подслушано_страшное@overhear']),
    (CubeEmotionClass.ENJOYMENT, ['#Подслушано_счастье@overhear']),
    (CubeEmotionClass.SHAME, ['#Подслушано_стыдно@overhear']),
    (CubeEmotionClass.DISGUST, ['#Подслушано_фууу@overhear']),
]

for emotion, queries in tagsEmotionsMapping:
    def stripTags(text):
        return re.sub('<[^<]+?>', '', text)

    def makeApiRequest(offset, query, emotion=''):
        response = vk_api.wall.search(owner_id=-34215577, offset=offset, owners_only=True, count=100, query=query,
                                      version='5.69')
        return (response[0], [
            {"text": stripTags(item['text'].replace(query, '')), "emotion": emotion, "source_type": "vk",
             "source_name": "overhear"} for item in response[1:]])

    print('Processing started: ' + emotion)

    total_results = []

    for query in queries:
        results = []
        offset = 0

        count = makeApiRequest(0, query)[0]

        while len(results) < count:
            sleep(2)
            (count_, results_) = makeApiRequest(offset, query, emotion)
            results.extend(results_)
            offset += 100

        total_results.extend(results)

    df = pd.DataFrame(total_results)
    df.to_csv(emotion + '.csv', encoding='utf-8')

print('All done')