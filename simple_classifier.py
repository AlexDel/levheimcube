from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

from features import CountFearFeatures_body, CountFearFeatures_time

from data import getVkData

# Set to True if reloading is needed
reloadData = False
vkDataFrame = getVkData(force_reload=reloadData)


# Estimating features
vkDataFrame['body_ratio'] = vkDataFrame['normalized_text'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['normalized_text'].apply(CountFearFeatures_time)

# Uncomment this for debugging
#vkDataFrame = vkDataFrame.sample(frac=0.1)

vkGrouped = vkDataFrame.groupby('emotion')


#Clasifier itslef#
X = vkDataFrame.loc[:, ['body_ratio', 'time_ratio']].values

labelEncoder = preprocessing.LabelEncoder()
y = labelEncoder\
    .fit(vkDataFrame['emotion'].unique())\
    .transform(vkDataFrame['emotion'].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

classifier = LinearSVC(class_weight='balanced')
classifier.fit(X_train, y_train)

y_predictions = classifier.predict(X_test)

report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)
print(report)