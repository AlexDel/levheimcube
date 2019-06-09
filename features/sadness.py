

def CountDistressFeatures_sadness(tokens=[]):

    sadnessTokens = ['грусть', 'грустный', 'грустить', 'грустно','загрустить']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in sadnessTokens:
            counter +=1

    # if counter >0: print('SADNESS')

    return counter / len(tokens)

def CountDistressFeatures_melancholy(tokens=[]):

    melancholyTokens = ['тоска','тосковать','тоскливо','тоскливый']


    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in melancholyTokens:
            counter +=1

    # if counter >0: print('melancholy')

    return counter / len(tokens)

def CountDistressFeatures_sad(tokens=[]):

    sadTokens = ['печаль','печально','печальный','печалить','печалиться','опечалить','опечаливать']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in sadTokens:
            counter +=1

    # if counter >0: print('SAD')

    return counter / len(tokens)

def CountDistressFeatures_distress(tokens=[]):

    distressTokens = ['огорчить','огорчать','огорчиться','огорченно','огорченный','огорчение']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in distressTokens:
            counter +=1

    # if counter >0: print('DISTRESS')

    return counter / len(tokens)

def CountDistressFeatures_gloomy(tokens=[]):

    gloomyTokens = ['угрюмо','угрюмый','угрюмиться']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in gloomyTokens:
            counter +=1

    # if counter >0: print('GLOOMY')

    return counter / len(tokens)

def CountDistressFeatures_despond(tokens=[]):

    despondTokens = ['унылый','уныло','уныние','унывать']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in despondTokens:
            counter +=1

    # if counter >0: print('DESPOND')

    return counter / len(tokens)

def CountDistressFeatures_upset(tokens=[]):

    upsetTokens = ['расстроить','расстроиться','расстроенно','расстроенный']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in upsetTokens:
            counter +=1

    # if counter > 0: print('UPSET')

    return counter / len(tokens)

def CountDistressFeatures_grim(tokens=[]):


    grimTokens = ['мрачный','мрачно','омрачить','помрачнеть','мрачнеть']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in grimTokens:
            counter +=1

    # if counter > 0: print('GRIM')

    return counter / len(tokens)

def CountDistressFeatures_glum(tokens=[]):

    glumTokens = ['хмурый','хмуро','хмурить','нахмурить','нахмуриться','хмуриться']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in glumTokens:
            counter +=1

    # if counter > 0: print('GLUM')

    return counter / len(tokens)

def CountDistressFeatures_pity(tokens=[]):

    pityTokens = ['жалость','жалеть','пожалеть','жалко','жалкий','жалобно','жалобный']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in pityTokens:
            counter +=1

    # if counter >0: print('PITY')

    return counter / len(tokens)

def CountDistressFeatures_tears(tokens=[]):


    tearsTokens = ['плакать', 'заплакать','проплакать','оплакать','оплакивать','поплакать','расплакаться',
                   'зарыдать','разрыдаться','прорыдать','рыдать',
                   'реветь', 'зареветь','разреветься',
                   'рыдание','слеза','нюня','плакса',
                   'плачущий','заплакавший','проплакавший','оплакивающий','оплакавший','плакавший','рыдающий','рыдавший','зарыдавший','прорыдавший','разрыдавшийся','заплаканный',
                   'скулить', 'заскулить', 'поскулить', 'отчаяние', 'отчаяться', 'отчаиваться']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in tearsTokens:
            counter +=1

    # if counter >0: print('TEARS')

    return counter / len(tokens)
