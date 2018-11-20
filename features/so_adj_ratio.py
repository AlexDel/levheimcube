from nltk import  bigrams

def CountStartleFeatures_SoAdj(tokens_parsed=[]):
    soTokens = ['такой', 'так']

    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    tokens_pairs = bigrams(tokens_parsed)

    for first_token, next_token in tokens_pairs:
        if first_token[0] in soTokens and next_token[1] in ('ADJF', 'ADJS'):
                counter += 1

    return counter / len(tokens_parsed)

#uncomment to debug
#text = open('../data/overhear/startle.csv').read()
#CountStartleFeatures_SoAdj(text)
#kok