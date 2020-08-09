import re
import os
from time import sleep
from typing import List, Dict, Optional

import pandas as pd
import vk
import tqdm

from misc.types import tags_emotions_mapping
from misc.constants import CubeEmotionClass


class VkAPIDataScraper():
    def __init__(
            self,
            group: Dict,
            emotion_mapping: Optional[tags_emotions_mapping] = None,
            session_token: str = '',
    ):
        self.emotion_mapping = emotion_mapping
        self.group = group

        self.session = vk.Session(access_token=session_token)
        self.vk_api = vk.API(self.session)

        self.total_results = []

    def _strip_tags(self, text):
        return re.sub('<[^<]+?>', '', text)

    def _make_query_api_request(self, offset, query, emotion=''):
        response = self.vk_api.wall.search(owner_id=self.group['id'], offset=offset, owners_only=True, count=100, query=query, v='5.69')

        return (response[0], [
            {"text": self._strip_tags(item['text'].replace(query, '')), "emotion": emotion, "source_type": "vk",
             "source_name": self.group['slug']} for item in response[1:]])

    def _make_get_all_posts_request(self, offset):
        response = self.vk_api.wall.get(owner_id=self.group['id'], offset=offset, owners_only=True, count=100, v='5.69')

        return (response, [
            {"text": self._strip_tags(item['text']), "emotion": None, "source_type": "vk",
             "source_name": self.group['id']} for item in response['items']])

    def fetch_results_by_emotion_mapping(self) -> List:
        for emotion, queries in self.emotion_mapping:
            print('Processing started: ' + emotion.value)

            result_for_emotion = []

            for query in queries:
                results = []
                offset = 0

                count = self._make_query_api_request(0, query)[0]

                while len(results) < count:
                    sleep(2)
                    (count_, results_) = self._make_query_api_request(offset, query, emotion.value)
                    results.extend(results_)
                    offset += 100

                result_for_emotion.extend(results)

            self.total_results.extend(result_for_emotion)

        print('All done')

        return self.total_results

    def fetch_all_results(self) -> List:
        results = []
        offset = 0

        print('Processing started... ')

        count = self._make_get_all_posts_request(0)[0]['count']

        pbar = tqdm.tqdm(total=count)

        while len(results) < count:
            sleep(2)
            (count_, results_) = self._make_get_all_posts_request(offset)
            results.extend(results_)
            offset += 100
            pbar.update(100)

        self.total_results = results

        print('All done')

        return self.total_results


    def export_to_csv(self, folder_path: str = ''):
        resultsDf = pd.DataFrame(self.total_results)

        if self.emotion_mapping == None:
            path = os.path.join(folder_path, f'UNTAGGED_{self.group["slug"]}.csv')
            resultsDf.to_csv(path, encoding='utf-8', index=False)
            return

        for emotion in resultsDf['emotion'].unique():
            path = os.path.join(folder_path, f'{emotion}_{self.group["slug"]}.csv')
            emotion_df = resultsDf[resultsDf['emotion'] == emotion]
            emotion_df.reset_index(drop=True).to_csv(path, encoding='utf-8', index=False)
            return
