def CountFearFeatures_family(tokens=[]):
    familyTokens = ['мама', 'папа', 'брат', 'сестра', 'дочь','сын','ребенок','бабушка','дедушка','тетя','дядя', 'семья']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in familyTokens:
            counter +=1

    return counter / len(tokens)
