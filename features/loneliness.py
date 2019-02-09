def CountFearFeatures_myself(tokens=[]):
    myselfTokens = ['себя', 'сам']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in myselfTokens:
            counter +=1

    return counter / len(tokens)

def CountFearFeatures_loneliness(tokens=[]):
    lonelinessTokens = ['одиночество', 'одинокий','одиноко']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in lonelinessTokens:
            counter +=1

    return counter / len(tokens)