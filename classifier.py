import csv
import codecs

import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
clf = MultinomialNB()

from analizer import normalize
vectorizer = CountVectorizer(analyzer=normalize)

samples = []
with codecs.open('./ready-data.tsv', 'r') as tsvFile:
  tsvReader = csv.DictReader(tsvFile, delimiter = '\t')
  for row in tsvReader:
    samples.append({'text': row['INPUT:text'], 'tag': row['OUTPUT:emotion']})

trainSet = vectorizer.fit_transform([t['text'] for t in samples])

clf.fit(trainSet, [t['tag'] for t in samples])


def most_informative_feature_for_class(vectorizer, classifier, classlabel, n=20):
  labelid = list(classifier.classes_).index(classlabel)
  feature_names = vectorizer.get_feature_names()
  topn = sorted(zip(classifier.feature_log_prob_[labelid], feature_names))[-n:]

  for coef, feat in topn:
    print(classlabel, feat, coef)

for emotion in set([t['tag'] for t in samples]):
  most_informative_feature_for_class(vectorizer, clf, emotion)