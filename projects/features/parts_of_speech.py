import pymorphy2

def CountStartleFeatures_Verb(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for token in tokens_parsed:
        if token[1] in ('VERB', 'INFN') and token[0].find('подслушано_') == -1:
            counter +=1

    return counter / len(tokens_parsed)

def CountStartleFeatures_adjectives(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for token in tokens_parsed:
        if token[1] in ('ADJS', 'ADJF') and token[0].find('подслушано_') == -1:
            counter +=1

    return counter / len(tokens_parsed)

def CountFearFeatures_numbers(punctuation_tokens=[]):
    counter = 0

    if len(punctuation_tokens) == 0:
        return 0

    morph = pymorphy2.MorphAnalyzer()

    for token in punctuation_tokens:
        p = morph.parse(token)[0]
        if 'NUMB' in p.tag:
            counter +=1

    return counter / len(punctuation_tokens)