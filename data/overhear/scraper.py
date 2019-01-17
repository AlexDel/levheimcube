import vk
import pandas as pd
import re
from time import sleep

session = vk.Session(access_token='')
vk_api = vk.API(session)

tagsEmotionsMapping = [
    ('anger', ['#Подслушано_БЕСИТ@overhear']),
    ('excitement', ['#Подслушано_успех@overhear']),
    ('distress', ['#Подслушано_одиночество@overhear']),
    ('startle', ['#Подслушано_странное@overhear', '#Подслушано_мистика@overhear']),
    ('fear', ['#Подслушано_страшное@overhear']),
    ('enjoyment', ['#Подслушано_счастье@overhear']),
    ('shame', ['#Подслушано_стыдно@overhear']),
    ('disgust', ['#Подслушано_фууу@overhear']),
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