import codecs
import csv

with codecs.open('./pism_text.txt', 'r', 'cp1251') as textFile:
    mainText = textFile.read()

letters = [{'INPUT:text':letter} for letter in mainText.split('\r\n\r\n?\r\n\r\n') if len(letter) > 0]

with open('./tasks.tsv', 'w') as tsvFile:
    tsvWriter = csv.DictWriter(tsvFile, fieldnames=['INPUT:text'], delimiter = '\t')
    tsvWriter.writeheader()
    tsvWriter.writerows(letters)
