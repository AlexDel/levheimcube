import vk
import pandas as pd
import re
from time import sleep

session = vk.Session(access_token='')
vk_api = vk.API(session)

results = []
offset = 0

def stripTags(text):
    return re.sub('<[^<]+?>', '', text)

def makeApiRequest(offset, query, label=''):
    response = vk_api.wall.search(owner_id=-34215577, offset=offset, owners_only=True, count=100, query=query, version='5.69')
    return (response[0], [{"text":stripTags(item['text'].replace(query, '')), "label": label } for item in response[1:]])

tagsEmotionsMapping = [
    ('#Подслушано_БЕСИТ@overhear', 'anger')
]

count = makeApiRequest(0, '#Подслушано_БЕСИТ@overhear')[0]

while len(results) < count:
    sleep(2)
    (count_, results_) = makeApiRequest(offset, '#Подслушано_БЕСИТ@overhear', 'anger')
    results.extend(results_)
    offset += 100

df = pd.DataFrame(results)
df.to_csv('anger.csv', encoding='utf-8')