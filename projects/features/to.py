import pymorphy2

def CountStartleFeatures_to(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)):
        if tokens_parsed[i].find('-то') != -1:
            counter +=1

    return counter / len(tokens_parsed)

