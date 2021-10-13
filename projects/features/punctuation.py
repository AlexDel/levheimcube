def CountStartleFeatures_exclamation(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i].find('!') != -1 and tokens_parsed[i].find('?!') == -1:
            counter +=1

    return counter / len(tokens_parsed)

def CountStartleFeatures_questionMark(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i].find('?') != -1 and tokens_parsed[i].find('?!') == -1:
            counter +=1

    return counter / len(tokens_parsed)

def CountStartleFeatures_supriseMark(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i].find('?!') != -1:
            counter +=1

    return counter / len(tokens_parsed)

def CountStartleFeatures_ellipsis(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i].find('...') != -1:
            counter +=1

    return counter / len(tokens_parsed)

def CountStartleFeatures_parcelling(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)-3):
        if tokens_parsed[i].find('!') != -1  or tokens_parsed[i].find('?') != -1 or tokens_parsed[i].find('.') != -1:
            if tokens_parsed[i+1].find('!') != -1 or tokens_parsed[i+1].find('?') != -1 or tokens_parsed[i+1].find('.') != -1 or tokens_parsed[i+2].find('!') != -1 or tokens_parsed[i+2].find('?') != -1 or tokens_parsed[i+2].find('.') != -1:
                if tokens_parsed[i+2].find('!') != -1 or tokens_parsed[i+2].find('?') != -1 or tokens_parsed[i+2].find('.') != -1 or tokens_parsed[i+3].find('!') != -1 or tokens_parsed[i+3].find('?') != -1 or tokens_parsed[i+3].find('.') != -1:
                    counter += 1

    return counter / len(tokens_parsed)

#uncomment to debug
# text = open('../data/overhear/ANGER_overhear.csv').read()
# print(CountStartleFeatures_exclamation(text))
#kok