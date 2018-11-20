import pymorphy2

def CountStartleFeatures_SoAdj(text):
    words = text.split()
    soTokens = ['такой', 'так']

    counter = 0
    morph = pymorphy2.MorphAnalyzer()

    if len(words) == 0:
        return 0
    for i in range(len(words)-1):
        if words[i].strip() in soTokens:
            p = morph.parse(words[i+1])[0]
            tag = p.tag.POS
            if tag == 'ADJF' or tag == 'ADJS':
                counter += 1
    return counter / (len(words) - 1)

#uncomment to debug
#text = open('../data/overhear/startle.csv').read()
#CountStartleFeatures_SoAdj(text)
#kok