import pymorphy2

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

morph = pymorphy2.MorphAnalyzer()

def normalize(text):
  tokens = [token for token in tokenizer.tokenize(text.lower())]
  tokens_parsed = [morph.parse(t)[0] for t in tokens]
  return [(t.normal_form, t.tag.POS) for t in tokens_parsed]
