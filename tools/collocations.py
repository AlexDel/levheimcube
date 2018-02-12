import sys
sys.path.insert(0, "..")

import pandas as pd

import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()

from analizer import normalize

dataPath = '../data/pismovnik/pismovnik-data.csv'
df = pd.read_csv(dataPath)

emotionsList = {}

for emotion in ['neutral', 'shame', 'distress', 'fear', 'anger', 'disgust', 'startle', 'enjoyment', 'excitement']:
    samples = normalize(''.join(df[df['emotion'] == emotion]['text']))
    emotionsList[emotion] = samples


for key in emotionsList.keys():
    finder = BigramCollocationFinder.from_words(emotionsList[key])
    finder.apply_freq_filter(3)
    print(key)
    print(finder.nbest(bigram_measures.student_t, 20))
