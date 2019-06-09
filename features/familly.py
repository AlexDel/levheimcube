def CountFearFeatures_family(tokens=[]):
    familyTokens = ['жена', 'муж', 'супруга', 'супруг', 'мама', 'мать', 'папа', 'отец', 'брат', 'сестра', 'дочь','сын','ребенок','бабушка','дедушка','тетя','дядя', 'семья', 'прабабушка', 'прадедушка', 'правнук', 'правнучка', 'внук','внучка','племянник','племянница']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in familyTokens:
            counter +=1

    return counter / len(tokens)
