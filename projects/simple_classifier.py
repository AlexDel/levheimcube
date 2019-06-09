from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier

from features import CountDistressFeatures_tears, CountDistressFeatures_sadness, CountDistressFeatures_melancholy, CountDistressFeatures_sad, CountDistressFeatures_distress, CountDistressFeatures_gloomy, CountDistressFeatures_despond, CountDistressFeatures_upset, CountDistressFeatures_grim, CountDistressFeatures_glum, CountDistressFeatures_pity, CountFearFeatures_caps, CountFearFeatures_numbers, CountFearFeatures_adjSuperb, CountFearFeatures_adjComparative, CountFearFeatures_absoluteness, CountFearFeatures_physiologicalActions, CountFearFeatures_talk_myself,CountFearFeatures_they_talk, CountFearFeatures_colon_talk, CountFearFeatures_what_talk, CountFearFeatures_death, CountStartleFeatures_supriseMark, CountStartleFeatures_exclamation, CountStartleFeatures_questionMark, CountFearFeatures_toldMe,CountFearFeatures_doctor_talk,CountFearFeatures_talk,CountFearFeatures_emphasizers,CountFearFeatures_myself, CountFearFeatures_loneliness, CountStartleFeatures_parcelling, CountFearFeatures_whenPeople, CountStartleFeatures_ellipsis, CountStartleFeatures_adjectives, CountStartleFeatures_Verb, CountFearFeatures_body, CountFearFeatures_time, CountStartleFeatures_soAdj, CountStartleFeatures_negative, CountStartleFeatures_soAdverbs, CountStartleFeatures_question_words, CountFearFeatures_illness, CountFearFeatures_family, CountFearFeatures_unreliableSpeech, CountStartleFeatures_to

from data import getVkData

RANDOM_STATE = 1488

# Set to True if reloading is needed
reloadData = False
vkDataFrame = getVkData(force_reload=reloadData)

# Estimating features

vkDataFrame['body_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_body)
vkDataFrame['time_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_time)


#NEW
vkDataFrame['adjComp_ratio'] = vkDataFrame['parsed_tokens'].apply(CountFearFeatures_adjComparative)
#vkDataFrame['adjSuperb_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_adjSuperb)  # работает долго, 15 мин

#
# Parts of speech
vkDataFrame['verb_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_Verb)
vkDataFrame['adjective_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_adjectives)
#vkDataFrame['numbers_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_numbers)  # работает долго, 15 мин
vkDataFrame['caps_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_caps)

# Galya sadness markers
vkDataFrame['sadness_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_sadness)
vkDataFrame['melancholy_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_melancholy)
vkDataFrame['sad_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_sad)
vkDataFrame['distress_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_distress)
vkDataFrame['gloomy_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_gloomy)
vkDataFrame['despond_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_despond)
vkDataFrame['upset_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_upset)
vkDataFrame['grim_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_grim)
vkDataFrame['glum_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_glum)
vkDataFrame['pity_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_pity)
vkDataFrame['tears_ratio'] = vkDataFrame['normal_tokens'].apply(CountDistressFeatures_tears)

# Тестирование для статьи
vkDataFrame['so_adj_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_soAdj)
vkDataFrame['so_advb_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_soAdverbs)
vkDataFrame['negative_ratio'] = vkDataFrame['parsed_tokens'].apply(CountStartleFeatures_negative)
vkDataFrame['questionMark_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_questionMark)
vkDataFrame['exclamation_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_exclamation)
vkDataFrame['surprise_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_supriseMark)
vkDataFrame['ellipsis_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_ellipsis)
vkDataFrame['parcelling_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_parcelling) #Doubtful?
vkDataFrame['questions_ratio'] = vkDataFrame['normal_tokens'].apply(CountStartleFeatures_question_words) #search for question words, separately decreases shame
vkDataFrame['illness_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_illness) #search for words reffered to illness, separately decreases shame
vkDataFrame['death_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_death)
vkDataFrame['family_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_family)
vkDataFrame['loneliness_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_loneliness) #very useful for distress
vkDataFrame['whenPeople_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_whenPeople)
vkDataFrame['to_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountStartleFeatures_to)
vkDataFrame['emphasizers_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_emphasizers)
vkDataFrame['myself_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_myself)
vkDataFrame['talk_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_talk)
vkDataFrame['unreliableSpeech_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_unreliableSpeech) #separately decreases shame -2 increases startle +1
#
#
# # Markers for talk
vkDataFrame['doctorTalk_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_doctor_talk)   #2
vkDataFrame['whatTalk_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_what_talk) #говорить, что #3
vkDataFrame['colonTalk_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_colon_talk)    #4
vkDataFrame['toldMe_ratio'] = vkDataFrame['punctuation_tokens'].apply(CountFearFeatures_toldMe) #7
vkDataFrame['theyTalk_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_they_talk) #8
vkDataFrame['talkMyself_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_talk_myself) #9
vkDataFrame['physiologicalActions_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_physiologicalActions)
vkDataFrame['absoluteness_ratio'] = vkDataFrame['normal_tokens'].apply(CountFearFeatures_absoluteness)


# Uncomment this for debugging
#vkDataFrame = vkDataFrame.sample(frac=0.1)

vkGrouped = vkDataFrame.groupby('emotion')


# Clasifier itslef#
#

X = vkDataFrame.loc[:, ['sadness_ratio','melancholy_ratio','sad_ratio','distress_ratio','gloomy_ratio','despond_ratio','upset_ratio','grim_ratio','glum_ratio','pity_ratio','tears_ratio','adjective_ratio','verb_ratio','absoluteness_ratio','physiologicalActions_ratio','talkMyself_ratio','doctorTalk_ratio','whatTalk_ratio','colonTalk_ratio','toldMe_ratio','theyTalk_ratio','unreliableSpeech_ratio','talk_ratio','to_ratio','whenPeople_ratio','questions_ratio','so_adj_ratio','so_advb_ratio','negative_ratio','body_ratio','time_ratio','family_ratio','illness_ratio','death_ratio','loneliness_ratio','myself_ratio','emphasizers_ratio','parcelling_ratio','exclamation_ratio','questionMark_ratio','surprise_ratio','ellipsis_ratio','caps_ratio','adjComp_ratio']].values   #Тестирование Алина

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