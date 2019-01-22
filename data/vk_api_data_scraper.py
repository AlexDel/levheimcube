import re
from time import sleep
from typing import List
import vk

from misc.types import tags_emotions_mapping, vk_group


def fetch_results_by_emotion_mapping(
    group: vk_group,
    emotion_mapping: tags_emotions_mapping,
    session_token:  str = '',
) -> List:

    session = vk.Session(access_token=session_token)
    vk_api = vk.API(session)

    total_results = []

    def stripTags(text):
        return re.sub('<[^<]+?>', '', text)

    def makeApiRequest(offset, query, emotion=''):
        response = vk_api.wall.search(owner_id=vk_group['id'], offset=offset, owners_only=True, count=100, query=query,
                                      version='5.69')
        return (response[0], [
            {"text": stripTags(item['text'].replace(query, '')), "emotion": emotion, "source_type": "vk",
             "source_name": vk_group['id']} for item in response[1:]])

    for emotion, queries in emotion_mapping:
        print('Processing started: ' + emotion.value)

        result_for_emotion = []

        for query in queries:
            results = []
            offset = 0

            count = makeApiRequest(0, query)[0]

            while len(results) < count:
                sleep(2)
                (count_, results_) = makeApiRequest(offset, query, emotion.value)
                results.extend(results_)
                offset += 100

            result_for_emotion.extend(results)

        total_results.extend(result_for_emotion)

    print('All done')

    return total_results
