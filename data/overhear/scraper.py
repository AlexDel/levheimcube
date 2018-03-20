import vk
import pandas as pd
import re
from time import sleep

session = vk.Session(access_token='')
vk_api = vk.API(session)

tagsEmotionsMapping = [
    ('#Подслушано_БЕСИТ@overhear', 'anger'),
    ('#Подслушано_успех@overhear', 'excitement'),
    ('#Подслушано_одиночество@overhear', 'distress'),
    ('#Подслушано_наблюдения@overhear', 'startle'),
    ('#Подслушано_страшное@overhear', 'fear'),
    ('#Подслушано_счастье@overhear', 'enjoyment'),
    ('#Подслушано_стыдно@overhear', 'shame'),
    ('#Подслушано_фууу@overhear', 'disgust'),
]

for query, emotion in tagsEmotionsMapping:
    print('Processing started: ' + query)
    results = []
    offset = 0

    def stripTags(text):
        return re.sub('<[^<]+?>', '', text)

    def makeApiRequest(offset, query, emotion=''):
        response = vk_api.wall.search(owner_id=-34215577, offset=offset, owners_only=True, count=100, query=query, version='5.69')
        return (response[0], [{"text":stripTags(item['text'].replace(query, '')), "emotion": emotion, "source_type": "vk", "source_name": "overhear" } for item in response[1:]])

    count = makeApiRequest(0, query)[0]

    while len(results) < count:
        sleep(2)
        (count_, results_) = makeApiRequest(offset, query, emotion)
        results.extend(results_)
        offset += 100

    df = pd.DataFrame(results)
    df.to_csv('anger.csv', encoding='utf-8')

print('All done')