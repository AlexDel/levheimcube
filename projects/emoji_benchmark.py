import pandas as pd
import numpy as np

from emoji import EMOJI_UNICODE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

from misc.constants import RANDOM_STATE
from projects.bag_of_words import bag_of_words_classifier, count_vect, labelEncoder
from data.caramel.loader import getCaramelData

# Toolchain preparation
nb_pipeline = make_pipeline(MultinomialNB())
nb_parameters = dict(multinomialnb__alpha=np.linspace(0.8, 1.0, num=5),
                     multinomialnb__fit_prior=[True, False])
cv = StratifiedKFold(n_splits=10)

def benchmark_features(dataframe: pd.DataFrame, feature_name: str) -> None:
    X = dataframe.loc[:, [feature_name]].values
    y = labelEncoder.transform(dataframe['emotion'].values)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=RANDOM_STATE)
    X_train = [x[0] for x in X_train.tolist()]
    X_test = [x[0] for x in X_test.tolist()]

    _vectorizer = TfidfVectorizer(analyzer=lambda x: x.split(), stop_words=None)
    X_train_vectors = _vectorizer.fit_transform(X_train)
    X_test_vectors = _vectorizer.transform(X_test)

    _model = GridSearchCV(nb_pipeline, param_grid=nb_parameters, scoring='precision_weighted', cv=cv)
    _model.fit(X_train_vectors, y_train)

    y_predictions = _model.predict(X_test_vectors)
    report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)

    print(feature_name)
    print(report)

# Fetching and labelling data
data = getCaramelData().to_dict('records')
data_emojies = [item for item in data if item['emoji'] != []]

predicted_emotions = bag_of_words_classifier.predict(count_vect.transform([entry['normal_tokens_as_string'] for entry in data_emojies]))
synthetically_labeled_data = list(map(lambda x: {**x[0], **{'emotion': labelEncoder.inverse_transform([x[1]])[0]}} , zip(data_emojies, predicted_emotions)))

emoji_df = pd.DataFrame(synthetically_labeled_data)
emoji_df['emojies_as_string'] = emoji_df['emoji'].apply(lambda x: ' '.join(x))
emoji_df['emojies_and_text_as_string'] = emoji_df['emojies_as_string'] + ' ' + emoji_df['normal_tokens_as_string']
emoji_df['emojies_and_text_as_string'] = emoji_df['emojies_as_string'] + ' ' + emoji_df['normal_tokens_as_string']


def convert_alias_to_emoji(string):
    try:
        return EMOJI_UNICODE[f':{string.replace(" ", "_")}:']
    except Exception:
        return



consistent_emojies = [
    'zipper-mouth face',
    'face with raised eyebrow',
    'neutral face',
    'expressionless face',
    'face without mouth',
    'smirking face',
    'unamused face',
    'face with rolling eyes',
    'grimacing face',
    'lying face',
    'face with medical mask',
    'face with thermometer',
    'face with head-bandage',
    'nauseated face',
    'face vomiting',
    'sneezing face',
    'hot face',
    'cold face',
    'woozy face',
    'dizzy face',
    'exploding head',
    'confused face',
    'worried face',
    'slightly frowning face',
    'frowning face',
    'face with open mouth',
    'hushed face',
    'astonished face',
    'flushed face',
    'pleading face',
    'frowning face with open mouth',
    'anguished face',
    'fearful face',
    'anxious face with sweat',
    'sad but relieved face',
    'crying face',
    'loudly crying face',
    'face screaming in fear',
    'confounded face',
    'persevering_face',
    'disappointed face',
    'face with steam from nose',
    'pouting face',
    'angry face',
    'face with symbols on mouth',
    'smiling face with horns',
    'angry face with horns',
    'skull',
    'skull and crossbones',
    'weary cat',
    'crying cat',
    'pouting cat',
    'see-no-evil monkey',
    'hear-no-evil monkey',
    'speak-no-evil monkey',
    'blue heart',
    'black heart',
    'thumbs down'
]

keys_of_consistent_emojis = list(map(convert_alias_to_emoji, consistent_emojies))

emoji_df['consistent_emojies_as_string'] = emoji_df['emoji'].apply(lambda x: ' '.join(list(filter(lambda x: x in keys_of_consistent_emojis, x))))
emoji_df['consistent_emojies_and_text_as_string'] = emoji_df['consistent_emojies_as_string'] + ' ' + emoji_df['normal_tokens_as_string']


# Start benchmarking
features_to_evaluate = [
    'emojies_as_string',
    'normal_tokens_as_string',
    'emojies_and_text_as_string',
    'consistent_emojies_and_text_as_string'
]

for feature_name in features_to_evaluate:
    benchmark_features(emoji_df, feature_name)
