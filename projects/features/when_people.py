def CountFearFeatures_whenPeople(tokens_parsed=[]):
    counter = 0

    if len(tokens_parsed) == 0:
        return 0

    for i in range(len(tokens_parsed)-2):
        if tokens_parsed[i].lower() == 'когда' and tokens_parsed[i+1] == 'люди' and tokens_parsed[i+2]:
            counter +=1

    return counter / len(tokens_parsed)