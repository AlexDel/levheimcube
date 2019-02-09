def CountFearFeatures_illness(tokens=[]):
    illnessTokens = ['врач', 'болезнь', 'боль', 'неизлечимый', 'неизлечимо','больница']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in illnessTokens:
            counter +=1

    return counter / len(tokens)