import re
import string

def CountStartleFeatures_SoAdj(text):
    text = re.sub('['+string.punctuation+']', '', text)    #removing punctuation from text
    words = text.lower().split()

    soTokens = ['такой', 'такого', 'такому', 'таким', 'таком', 'такая', 'такую', 'такой', 'такое']
    endings = ['ой', 'ый', 'ий', 'ого', 'его', 'ом', 'ему', 'ым', 'им', 'ем', 'ая', 'яя', 'ей', 'ую', 'юю', 'ей', 'ое', 'ее', 'ому' ]

    counter = 0

    if len(words) == 0:
        return 0
    for i in range(len(words)):
        if words[i].strip() in soTokens:
            if words[i+1].strip()[-2:] in endings:
                counter += 1
    return counter / len(words)

#text = open('../data/overhear/startle.csv').read() #uncomment to debug
#CountStartleFeatures_SoAdj(text)