def CountFearFeatures_absoluteness(tokens=[]):
    absolutenessTokens = ['всегда', 'никогда', 'всюду', 'повсюду', 'нигде', 'все', 'никто', 'ничто', 'ничего', 'всякий', 'никакой', 'ни один', 'ни одна']

    counter = 0

    if len(tokens) == 0:
        return 0
    for token in tokens:
        if token in absolutenessTokens:
            counter +=1
    return counter / len(tokens)