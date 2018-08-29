from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import precision_score

from data import vkDataFrame
from features import CountFearFeatures_body, CountFearFeatures_time

# Uncomment this for debugging
#vkDataFrame = vkDataFrame.sample(frac=0.1)

vkDataFrame['body_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['text'].apply(CountFearFeatures_time)

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

print(labelEncoder.inverse_transform(list(set(y_test) - set(y_predictions)))) # Эти классы не распознаются классификатором

precision = precision_score(y_test, y_predictions, average='weighted')
print('\n Precision score: {0}'.format(precision))