import pandas as pd

from data import vkDataFrame
from features import CountFearFeatures_body, CountFearFeatures_time

vkDataFrame['body_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_time)

print('Структура таблицы:')
print(vkDataFrame.info())

print('Первые 5 элементов:')
print(vkDataFrame.loc[:, ['text', 'body_ratio', 'time_ratio', 'emotion']].head())

vkGrouped = vkDataFrame.groupby('emotion')

print('Статистика по частям тела:')
print(vkGrouped['body_ratio'].describe())

print('Статистика по времени:')
print(vkGrouped['time_ratio'].describe())