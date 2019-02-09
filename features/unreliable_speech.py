import pymorphy2

def CountFearFeatures_unreliableSpeech(tokens=[]):
    unreliableSpeechTokens = ['якобы', 'мол', 'дескать']

    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token in unreliableSpeechTokens:
            counter +=1

    return counter / len(tokens)
