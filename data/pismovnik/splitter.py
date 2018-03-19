import codecs
import csv
from random import shuffle

minParagraphLength = 300

with codecs.open('./pism_text.txt', 'r', 'cp1251') as textFile:
    mainText = textFile.read()

letters = [letter for letter in mainText.split('\r\n\r\n?\r\n\r\n') if len(letter) > 0]

paragraphs = []
for letter in letters:
    prs = letter.split('\r\n\r\n')
    for p in prs:
        if len(p) > minParagraphLength:
            paragraphs.append(p)

shuffle(paragraphs)

paragraphs = [{'INPUT:text': paragraph} for paragraph in paragraphs]

with open('./tasks.tsv', 'w') as tsvFile:
    tsvWriter = csv.DictWriter(tsvFile, fieldnames=['INPUT:text'], delimiter = '\t')
    tsvWriter.writeheader()
    tsvWriter.writerows(paragraphs)
