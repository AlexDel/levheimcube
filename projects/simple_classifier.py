from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier

from features import CountFearFeatures_body, CountFearFeatures_time, CountStartleFeatures_SoAdj

from data import getVkData

RANDOM_STATE = 1488

# Set to True if reloading is needed
reloadData = False
vkDataFrame = getVkData(force_reload=reloadData)


# Estimating features
vkDataFrame['body_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_time)
vkDataFrame['so_adj_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_SoAdj)

# Uncomment this for debugging
#vkDataFrame = vkDataFrame.sample(frac=0.1)

vkGrouped = vkDataFrame.groupby('emotion')


# Clasifier itslef#
X = vkDataFrame.loc[:, ['body_ratio', 'time_ratio','so_adj_ratio']].values

labelEncoder = preprocessing.LabelEncoder()
y = labelEncoder\
    .fit(vkDataFrame['emotion'].unique())\
    .transform(vkDataFrame['emotion'].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=RANDOM_STATE, stratify=y)

classifier = LinearSVC(class_weight='balanced', random_state=RANDOM_STATE)
classifier.fit(X_train, y_train)

y_predictions = classifier.predict(X_test)

report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)
print(report)

# Baseline classifier
dummyClf = DummyClassifier(strategy='uniform', random_state=RANDOM_STATE)
dummyClf.fit(X_train, y_train)

dummyPredictions = dummyClf.predict(X_test)
baselineReport = classification_report(y_test, dummyPredictions, target_names=labelEncoder.classes_)
print(baselineReport)