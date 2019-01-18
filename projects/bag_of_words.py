import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

from data import getVkData

RANDOM_STATE = 42

# Set to True if reloading is needed
reloadData = False
vkDataFrame = getVkData(force_reload=reloadData)


count_vect = CountVectorizer()

# Clasifier itslef#
X = vkDataFrame.loc[:, ['normal_tokens_as_string']].values

labelEncoder = preprocessing.LabelEncoder()
y = labelEncoder\
    .fit(vkDataFrame['emotion'].unique())\
    .transform(vkDataFrame['emotion'].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=RANDOM_STATE)

X_train = [x[0] for x in X_train.tolist()]
X_test =  [x[0] for x in X_test.tolist()]

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
X_test_counts = count_vect.transform(X_test)

nb_pipeline = make_pipeline(MultinomialNB())
nb_parameters = dict(multinomialnb__alpha=np.linspace(0.8, 1.0, num=5),
                     multinomialnb__fit_prior=[True, False])
cv = StratifiedKFold(n_splits=10)

model = GridSearchCV(nb_pipeline, param_grid=nb_parameters, scoring='precision_weighted', cv=cv)

model.fit(X_train_counts,  y_train)

y_predictions = model.predict(X_test_counts)

report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)
print(report)
