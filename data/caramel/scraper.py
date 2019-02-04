import os

from misc.constants import CubeEmotionClass
from misc.types import tags_emotions_mapping

from data.vk_api_data_scraper import VkAPIDataScraper

overhear_public = {
    'id': -93330757,
    'slug': 'caramel'
}

scraper = VkAPIDataScraper(overhear_public, None, '')
scraper.fetch_all_results()
scraper.export_to_csv(os.getcwd())
