import pymorphy2

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

morph = pymorphy2.MorphAnalyzer()

def normalize(text):
  tokens = [token for token in tokenizer.tokenize(text.lower())]
  tokens_parsed = [morph.parse(t)[0] for t in tokens]
  return [(str(t.normal_form), str(t.tag.POS)) for t in tokens_parsed]

def not_normalize(text):
  tokens = [token for token in text.split()]
  return [t for t in tokens]