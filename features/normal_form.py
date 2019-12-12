import pymorphy2
import string
import re

morph = pymorphy2.MorphAnalyzer()
p = morph.parse('говорят')[0]
lemma = p.normal_form
print(lemma)
print(p.tag)
print(str(p.normal_form))
print(p.tag.tense)

if 'Supr' in p.tag:
    print('Превосходная')

# import re
# s = 'сказали,'
# s = re.sub(r'[^\w\s]','',s)
# print(s)
from nltk.tokenize import regexp_tokenize
print(regexp_tokenize("Can't is a 11 contraction.", "[\w']+"))

counter = 0
punctuation_tokens = ['МАМА', 'мапр', 'МАрШ']
for token in punctuation_tokens:

    for n in token:
        if n.isupper():
            counter = counter + 1

print(morph.parse('Девять')[0])