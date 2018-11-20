import pymorphy2
import nltk

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

from nltk.corpus import stopwords
stop_words = stopwords.words('russian')
other_stopwords = ['это', 'который', 'тот', 'весь', 'свой', 'наш', 'ещё', 'нея', 'мочь']
stop_words.extend(other_stopwords)

morph = pymorphy2.MorphAnalyzer()

def strip_stopwords(text):
  tokens = [token for token in tokenizer.tokenize(text.lower())]
  tokens = [morph.parse(t)[0].normal_form for t in tokens ]
  return [t for t in tokens]

def normalize(text):
  tokens = [token for token in tokenizer.tokenize(text.lower())]
  tokens = [morph.parse(t)[0].normal_form for t in tokens ]
  return [t for t in tokens if t not in stop_words]

def normalize2(text):
  tokens = [token for token in tokenizer.tokenize(text.lower())]
  tokens = [morph.parse(t)[0].normal_form for t in tokens ]
  return [t for t in tokens if t not in stop_words]