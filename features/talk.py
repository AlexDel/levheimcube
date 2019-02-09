from nltk import  bigrams

def CountFearFeatures_talk(tokens=[]):
    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token == 'говорить':
            #print(token)
            counter +=1

    return counter / len(tokens)

def CountFearFeatures_pronoun_talk(tokens=[]):
    soTokens = ['он', 'она', 'они']

    counter = 0

    if len(tokens) == 0:
        return 0

    tokens_pairs = bigrams(tokens)

    for first_token, next_token in tokens_pairs:
        if first_token[0] in soTokens and next_token[1] == 'говорить':
            counter += 1

    return counter / len(tokens)