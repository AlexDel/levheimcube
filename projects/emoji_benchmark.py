import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

from misc.constants import RANDOM_STATE
from projects.bag_of_words import bag_of_words_classifier, count_vect, labelEncoder
from data.caramel.loader import getCaramelData

# Fetching and labelling data
data = getCaramelData().to_dict('records')
data_emojies = [item for item in data if item['emoji'] != []]

predicted_emotions = bag_of_words_classifier.predict(count_vect.transform([entry['normal_tokens_as_string'] for entry in data_emojies]))
synthetically_labeled_data = list(map(lambda x: {**x[0], **{'emotion': labelEncoder.inverse_transform([x[1]])[0]}} , zip(data_emojies, predicted_emotions)))
emoji_df = pd.DataFrame(synthetically_labeled_data)
emoji_df['emojies_as_string'] = emoji_df['emoji'].apply(lambda x: ' '.join(x))

# Toolchain preparation
nb_pipeline = make_pipeline(MultinomialNB())
nb_parameters = dict(multinomialnb__alpha=np.linspace(0.8, 1.0, num=5),
                     multinomialnb__fit_prior=[True, False])
cv = StratifiedKFold(n_splits=10)

# Pure emoji model (PE)
X = emoji_df.loc[:, ['emojies_as_string']].values
y = labelEncoder.transform(emoji_df['emotion'].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=RANDOM_STATE)
X_train = [x[0] for x in X_train.tolist()]
X_test =  [x[0] for x in X_test.tolist()]

emoji_vectorizer = TfidfVectorizer(analyzer=lambda x: x.split(), stop_words=None)
X_train_vectors = emoji_vectorizer.fit_transform(X_train)
X_test_vectors = emoji_vectorizer.transform(X_test)

PE_model = GridSearchCV(nb_pipeline, param_grid=nb_parameters, scoring='precision_weighted', cv=cv)
PE_model.fit(X_train_vectors, y_train)


#Merged Emojies and Words



if __name__ == "__main__":
    print('Pure emojies benchmarking')

    y_predictions = PE_model.predict(X_test_vectors)
    report = classification_report(y_test, y_predictions, target_names=labelEncoder.classes_)
    print(report)