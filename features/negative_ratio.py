def CountStartleFeatures_negative(tokens_parsed=[]):
    negativeTokens = ['не', 'нет', 'нее']

    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i][0] in negativeTokens:
            counter +=1

    return counter / len(tokens_parsed)

