import pymorphy2
import csv
import codecs
import nltk

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

from nltk.corpus import stopwords
stop_words = stopwords.words('russian')

morph = pymorphy2.MorphAnalyzer()

samples = []
with codecs.open('./ready-data.tsv', 'r') as tsvFile:
  tsvReader = csv.DictReader(tsvFile, delimiter = '\t')
  for row in tsvReader:
    samples.append({'text': row['INPUT:text'], 'tag': row['OUTPUT:emotion']})

def normalize(text):
  tokens = [token for token in tokenizer.tokenize(text.lower()) if token not in stop_words]
  return [morph.parse(t)[0].normal_form for t in tokens]

def getData():
  normalizedData = []
  for s in samples:
    normalizedData.append({'words': normalize(s['text']), 'tag': s['tag']})

  return normalizedData