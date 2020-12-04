import pandas as pd
import numpy as np

from sklearn import preprocessing, svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

np.random.seed(31415) 

df_train = pd.read_csv('https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.train.csv')
df_test = pd.read_csv('https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.test.csv')

labelEncoder = preprocessing.LabelEncoder().fit(df_train['emotion'].unique())
y_train = labelEncoder.transform(df_train['emotion'].values)
y_test = labelEncoder.transform(df_test['emotion'].values)

X_train = df_train.loc[:, ['text']].values
X_test =  df_test.loc[:, ['text']].values

# transforming text to tfIdf vectors of char n-grams
tfIdf_vect = TfidfVectorizer(analyzer='char',ngram_range=(5,5), max_df=0.8)
X_train_counts = tfIdf_vect.fit_transform([x[0] for x in X_train.tolist()])
X_test_counts = tfIdf_vect.transform([x[0] for x in X_test.tolist()])

# Making a LinearSVC classifier
classifier = svm.LinearSVC(class_weight='balanced')
classifier.fit(X_train_counts, y_train)

y_predictions = classifier.predict(X_test_counts)

report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)
print(report)