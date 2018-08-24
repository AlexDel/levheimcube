from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

from data import vkDataFrame
from features import CountFearFeatures_body, CountFearFeatures_time

vkDataFrame['body_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_time)

#Some data and statistics

print('Структура таблицы:')
print(vkDataFrame.info())

print('Первые 5 элементов:')
print(vkDataFrame.loc[:, ['text', 'body_ratio', 'time_ratio', 'emotion']].head())

vkGrouped = vkDataFrame.groupby('emotion')

print('Статистика по частям тела:')
print(vkGrouped['body_ratio'].describe())

print('Статистика по времени:')
print(vkGrouped['time_ratio'].describe())

#Clasifier itslef#
X = vkDataFrame.loc[:, ['body_ratio', 'time_ratio']].values

labelEncoder = preprocessing.LabelEncoder()
y = labelEncoder\
    .fit(vkDataFrame['emotion'].unique())\
    .transform(vkDataFrame['emotion'].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

classifier = LinearSVC()
classifier.fit(X_train, y_train)

y_predictions = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_predictions)
print('Average precision-recall score: {0}'.format(accuracy))