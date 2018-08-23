import os

#Множество слов, связанных с телом (ПЕРЕДЕЛАТЬ)
body_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'body_spisok.txt'), 'r', encoding='utf-8')
body_list = body_file.read()
body_set = set()
for word in body_list.split(','):
    body_set.add(word.strip())
    print(word.strip())

#Функция, считающая долю лексики ЛСП "тело"
def CountFearFeatures_body(text):
    features_body_list = []

    if type(text) is not str:
        return 0

    words = text.lower().split()
    if len(words) == 0:
        return 0
    for word in words:
        if word.strip() in body_set:
            features_body_list.append(word.strip())
    return len(features_body_list) / len(words)