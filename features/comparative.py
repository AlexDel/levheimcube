import pymorphy2
import re

def CountFearFeatures_adjComparative(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for token in tokens_parsed:
        if token[1] == 'COMP':
            counter +=1
    return counter / len(tokens_parsed)

def CountFearFeatures_adjSuperb(punctuation_tokens=[]):
    counter = 0

    if len(punctuation_tokens) == 0:
        return 0

    morph = pymorphy2.MorphAnalyzer()

    for token in punctuation_tokens:
        p = morph.parse(token)[0]
        if 'Supr' in p.tag:
            counter +=1

    return counter / len(punctuation_tokens)


def CountFearFeatures_caps(punctuation_tokens=[]):

    if len(punctuation_tokens) == 0:
        return 0

    counter = 0
    n = 0

    for token in punctuation_tokens:

        for l in re.sub(r'[^\w\s]','',token):
            if l.isupper():
                counter = counter + 1
            else:
                counter = 0
        if counter > 1:
            n = n + 1

    return n / len(punctuation_tokens)

#CountFearFeatures_caps(['МАМА:', 'мапр', 'МАрШ', 'НАРк','Шок'])
