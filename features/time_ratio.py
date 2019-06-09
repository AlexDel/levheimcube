#from tools.normalizer import normalize

#Функция, считающая долю лексики с семой "короткий промежуток времени"
def CountFearFeatures_time(tokens=[]):
    features_time_list = []

    timeTokens = ['день', 'секунда', 'момент','час']

    words = tokens
    if len(words) == 0:
        return 0
    for word in words:
        if word in timeTokens:
            features_time_list.append(word)
    return len(features_time_list) / len(words)