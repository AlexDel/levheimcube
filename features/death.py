def CountFearFeatures_death(tokens=[]):
    deathTokens = ['смерть', 'умирать', 'умереть', 'могила', 'похороны','кладбище','оплакивать','оплакать', 'скорбеть','хоронить','похоронить','скончаться','захоронить','погибнуть','погибать','кремировать','осиротеть']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in deathTokens:
            counter +=1

    return counter / len(tokens)