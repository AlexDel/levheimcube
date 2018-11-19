import pymorphy2

def CountStartleFeatures_SoAdj(tokens_parsed=[]):
    soTokens = ['такой', 'так']

    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i, t in enumerate(tokens_parsed):
        current_token = tokens_parsed[i][0]
        next_token_pos_tag = tokens_parsed[i+1][1]
        if current_token in soTokens and next_token_pos_tag in ('ADJF', 'ADJS'):
                counter += 1

    return counter / len(tokens_parsed)

#uncomment to debug
#text = open('../data/overhear/startle.csv').read()
#CountStartleFeatures_SoAdj(text)
#kok