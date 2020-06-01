import requests
import csv
import os
from bs4 import BeautifulSoup
from time import sleep


class WikiAPIDataScraper:
    def __init__(self):
        self.total_results = []

    def make_requests(self, count):
        url = "https://ru.wikipedia.org/api/rest_v1/page/random/html"
        responses = []

        for i in range(0, count):
            response = requests.get(url)
            if response.status_code == 200:
                responses.append(response)
            sleep(1)

        result = []

        for response in responses:
            soup = BeautifulSoup(response.content, "html.parser")
            for paragraph in soup.find_all("p"):
                if 3000 > len(paragraph.text) > 0:
                    result.append({'text': paragraph.text})

        self.total_results = result

    def export_to_csv(self, folder_path: str = ''):
        path = os.path.join(folder_path, "wiki.csv")
        with open(path, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['text'])
            writer.writeheader()
            writer.writerows(self.total_results)


scraper = WikiAPIDataScraper()
scraper.make_requests(300)
scraper.export_to_csv(os.getcwd())