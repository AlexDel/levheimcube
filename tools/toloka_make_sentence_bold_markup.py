import pandas as pd
from nltk import sent_tokenize

df = pd.read_csv('./task_sentences.tsv', sep='\t')

result = []

for index, row in df.iterrows():
    sentences = sent_tokenize(row['INPUT:text'])
    for i, sent in enumerate(sentences):
        result.append({
            'INPUT:text': ''.join([*sentences[:i], f'<b>{sent}</b>', *sentences[i+1:]]),
            'INPUT:type': 'PART',
            'INPUT:emotion': row['INPUT:emotion']
        })

pd.DataFrame(result).to_csv('tasks_text_partial.tsv', sep='\t', index=False)
