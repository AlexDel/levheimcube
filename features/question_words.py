import pymorphy2

def CountStartleFeatures_question_words(tokens=[]):
    questionTokens = ['кто','что','почему','где','как','куда','откуда','когда','какой','чей','отчего','зачем','сколько','кого']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in questionTokens:
            counter +=1

    return counter / len(tokens)

#uncomment to debug
#text = open('../data/overhear/startle.csv').read()
#CountStartleFeatures_question_words(text)
