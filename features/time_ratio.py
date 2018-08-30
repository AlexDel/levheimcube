from tools.analizer import normalize

#Функция, считающая долю лексики с семой "короткий промежуток времени"
def CountFearFeatures_time(text):
    features_time_list = []

    if type(text) is str:
        words = normalize(text)
    else:
        words = text

    timeTokens = ['день', 'секунда', 'момент','час']

    if len(words) == 0:
        return 0
    for word in words:
        if word in timeTokens:
            features_time_list.append(word)
    return len(features_time_list) / len(words)