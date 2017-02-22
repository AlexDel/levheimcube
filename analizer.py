import pymorphy2
import nltk

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

from nltk.corpus import stopwords
stop_words = stopwords.words('russian')
other_stopwords = ['это', 'который', 'тот', 'весь', 'свой', 'наш', 'ещё', 'нея', 'мочь']
stop_words.extend(other_stopwords)

morph = pymorphy2.MorphAnalyzer()

def normalize(text):
  tokens = [token for token in tokenizer.tokenize(text.lower())]
  normTokens = [morph.parse(t)[0].normal_form for t in tokens ]
  return [t for t in normTokens if t not in stop_words]
