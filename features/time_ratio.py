import re

#Функция, считающая долю лексики с семой "короткий промежуток времени"
def CountFearFeatures_time(text):
    features_time_list = []
    words = text.lower().split()
    if len(words) == 0:
        return 0
    for word in words:
        if re.match('^минут.*$', word):
            features_time_list.append(word)
        elif re.match('^секунд.*$', word):
            features_time_list.append(word)
        elif re.match('^момент.*$', word):
            features_time_list.append(word)
        elif re.match('^час.*$', word):
            features_time_list.append(word)
        elif re.match('^дн.+$', word):
            features_time_list.append(word)
        elif re.match('^ден.+$', word):
            features_time_list.append(word)
    return len(features_time_list) / len(words)