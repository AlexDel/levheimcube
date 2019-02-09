def CountStartleFeatures_pnct(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i].find('!') != -1  or tokens_parsed[i].find('?') != -1:
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

    for i in range(len(tokens_parsed)-2):
        if tokens_parsed[i].find('!') != -1  or tokens_parsed[i].find('?') != -1 or tokens_parsed[i].find('.') != -1:
            if tokens_parsed[i+1].find('!') != -1 or tokens_parsed[i+1].find('?') != -1 or tokens_parsed[i+1].find('.') != -1 or tokens_parsed[i+2].find('!') != -1 or tokens_parsed[i+2].find('?') != -1 or tokens_parsed[i+2].find('.') != -1:
                #print(tokens_parsed[i], ' ', tokens_parsed[i+1], ' ', tokens_parsed[i+2]) #uncomment for debug
                counter += 1

    return counter / len(tokens_parsed)