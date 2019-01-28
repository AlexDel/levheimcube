from typing import List

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from tools.stop_words import stop_words

def most_informative_feature_for_class(vectorizer, classifier, class_label, n=20):
    label_id = list(classifier.classes_).index(class_label)

    feature_names = vectorizer.get_feature_names()

    top_n = sorted(zip(classifier.feature_log_prob_[label_id], feature_names))[-n:]

    for coef, feat in top_n:
      print(class_label, feat, coef)


def get_n_most_informative_features(samples):
    clf = MultinomialNB()

    vectorizer = TfidfVectorizer(stop_words=stop_words)

    train_set = vectorizer.fit_transform([t['normal_tokens_as_string'] for t in samples])

    clf.fit(train_set, [t['emotion'] for t in samples])

    for emotion in set([t['emotion'] for t in samples]):
        most_informative_feature_for_class(vectorizer, clf, emotion)
