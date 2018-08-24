import pandas as pd

from data import vkDataFrame
from features import CountFearFeatures_body, CountFearFeatures_time

vkDataFrame['body_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_body)

print('Структура таблицы:')
print(vkDataFrame.info())

print('Первые 5 элементов:')
print(vkDataFrame.loc[:, ['text', 'body_ratio', 'emotion']].head())

print('Статистика по частям тела:')
print(vkDataFrame['body_ratio'].describe())