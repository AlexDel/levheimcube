import pandas as pd
import re
from time import sleep
import vk

from misc.types import tags_emotions_mapping


def fetch_results_by_emotion_mapping(
    group_id: int,
    emotion_mapping: tags_emotions_mapping,
    session_token:  str = '',
) -> pd.DataFrame:

    session = vk.Session(access_token=session_token)
    vk_api = vk.API(session)

    df = pd.DataFrame([])

    def stripTags(text):
        return re.sub('<[^<]+?>', '', text)

    def makeApiRequest(offset, query, emotion=''):
        response = vk_api.wall.search(owner_id=group_id, offset=offset, owners_only=True, count=100, query=query,
                                      version='5.69')
        return (response[0], [
            {"text": stripTags(item['text'].replace(query, '')), "emotion": emotion, "source_type": "vk",
             "source_name": str(group_id)} for item in response[1:]])

    for emotion, queries in emotion_mapping:
        print('Processing started: ' + emotion.value)

        total_results = []

        for query in queries:
            results = []
            offset = 0

            count = makeApiRequest(0, query)[0]

            while len(results) < count:
                sleep(2)
                (count_, results_) = makeApiRequest(offset, query, emotion.value)
                results.extend(results_)
                offset += 100

            total_results.extend(results)

        df.append(total_results)

    print('All done')

    return df
