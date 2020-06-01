import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline


df_train = pd.read_csv('https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.train.csv')
df_test = pd.read_csv('https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.test.csv')

labelEncoder = preprocessing.LabelEncoder().fit(df_train['emotion'].unique())
y_train = labelEncoder.transform(df_train['emotion'].values)
y_test = labelEncoder.transform(df_test['emotion'].values)

X_train = df_train.loc[:, ['text']].values
X_test =  df_test.loc[:, ['text']].values

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform([x[0] for x in X_train.tolist()])
X_test_counts = count_vect.transform([x[0] for x in X_test.tolist()])

nb_pipeline = make_pipeline(MultinomialNB())
nb_parameters = dict(multinomialnb__alpha=np.linspace(0.8, 1.0, num=5),
                     multinomialnb__fit_prior=[True, False])
cv = StratifiedKFold(n_splits=10)

model = GridSearchCV(nb_pipeline, param_grid=nb_parameters, scoring='precision_weighted', cv=cv)

model.fit(X_train_counts,  y_train)

bag_of_words_classifier = model

if __name__ == "__main__":
    y_predictions = model.predict(X_test_counts)

    report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)
    print(report)
