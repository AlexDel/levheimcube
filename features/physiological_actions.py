def CountFearFeatures_physiologicalActions(tokens=[]):
    actionsTokens = ['сморкаться', 'дышать', 'хрипеть', 'глотать', 'потеть', 'кашлять', 'чихать', 'сопеть', 'кряхтеть', 'отлить', 'рыгать', 'давиться', 'пукать', 'отрыгивать', 'спать', 'дремать', 'есть', 'жевать', 'чавкать', 'трахать']

    counter = 0

    if len(tokens) == 0:
        return 0
    for token in tokens:
        if token in actionsTokens:
            counter +=1
    return counter / len(tokens)