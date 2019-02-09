from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier

from features import CountFearFeatures_pronoun_talk, CountFearFeatures_talk,CountFearFeatures_emphasizers,CountFearFeatures_myself, CountFearFeatures_loneliness, CountStartleFeatures_parcelling, CountFearFeatures_whenPeople, CountStartleFeatures_ellipsis, CountStartleFeatures_adjectives, CountStartleFeatures_Verb, CountFearFeatures_body, CountFearFeatures_time, CountStartleFeatures_soAdj, CountStartleFeatures_negative, CountStartleFeatures_soAdverbs, CountStartleFeatures_pnct, CountStartleFeatures_question_words, CountFearFeatures_illness, CountFearFeatures_family, CountFearFeatures_unreliableSpeech, CountStartleFeatures_to


from data import getVkData

RANDOM_STATE = 1488

# Set to True if reloading is needed
reloadData = False
vkDataFrame = getVkData(force_reload=reloadData)

# Estimating features

#Doubtfuly useful
vkDataFrame['unreliableSpeech_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_unreliableSpeech) #separately decreases shame -2 increases startle +1
vkDataFrame['ellipsis_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_ellipsis)
vkDataFrame['myself_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_myself)
vkDataFrame['emphasizers_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_emphasizers)

# Together more or less useful
vkDataFrame['whenPeople_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_whenPeople)
vkDataFrame['to_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_to)

#Useful
vkDataFrame['body_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_time)
vkDataFrame['so_adj_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_soAdj)
vkDataFrame['so_advb_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_soAdverbs)
vkDataFrame['negative_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_negative)
vkDataFrame['punctuation_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_pnct)
vkDataFrame['questions_ratio'] = vkDataFrame['normal_tokens'].apply(CountStartleFeatures_question_words) #search for question words, separately decreases shame
vkDataFrame['illness_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_illness) #search for words reffered to illness, separately decreases shame
vkDataFrame['family_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_family)
vkDataFrame['parcelling_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_parcelling) #Doubtful?
vkDataFrame['loneliness_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_loneliness) #very useful foe distress

#Not tested
vkDataFrame['talk_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_talk)

#Parts of speech
vkDataFrame['verb_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_Verb)
vkDataFrame['adjective_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_adjectives)


# Uncomment this for debugging
#vkDataFrame = vkDataFrame.sample(frac=0.1)

vkGrouped = vkDataFrame.groupby('emotion')


# Clasifier itslef#
#X = vkDataFrame.loc[:, ['body_ratio','time_ratio','so_adj_ratio','so_advb_ratio','negative_ratio','punctuation_ratio','family_ratio','illness_ratio','questions_ratio','whenPeople_ratio','to_ratio','parcelling_ratio','loneliness_ratio']].values

#X = vkDataFrame.loc[:, ['body_ratio','time_ratio','so_adj_ratio','so_advb_ratio','negative_ratio','punctuation_ratio','family_ratio','illness_ratio','questions_ratio','loneliness_ratio','talk_ratio',]].values #База №1
X = vkDataFrame.loc[:, ['body_ratio','time_ratio','so_adj_ratio','so_advb_ratio','negative_ratio','punctuation_ratio','family_ratio','illness_ratio','questions_ratio','whenPeople_ratio','to_ratio','parcelling_ratio','loneliness_ratio','talk_ratio','emphasizers_ratio']].values #База №2

#X = vkDataFrame.loc[:, ['talk_ratio']].values #for 1 function testing #solo testing

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