from nltk import  bigrams
import pymorphy2

def CountStartleFeatures_soAdj(tokens_parsed=[]):
    soTokens = ['такой', 'так']

    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    tokens_pairs = bigrams(tokens_parsed)

    for first_token, next_token in tokens_pairs:
        if first_token[0] in soTokens and next_token[1] in ('ADJF', 'ADJS'):
            counter += 1

    return counter / len(tokens_parsed)

def CountStartleFeatures_soAdverbs(tokens_parsed=[]):
    soTokens = ['так']

    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    tokens_pairs = bigrams(tokens_parsed)

    for first_token, next_token in tokens_pairs:
        if first_token[0] in soTokens and next_token[1] in ('ADVB'):
            counter += 1

    return counter / len(tokens_parsed)