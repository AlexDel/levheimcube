import pandas as pd
from  scipy.spatial import distance

df = pd.DataFrame

df = pd.read_csv('https://storage.yandexcloud.net/nlp-dataset-bucket-1/toloka-vk-proceedings-2020/toloka_recalc_lean.csv')

MAPPING = {
    'distress': [0, 1, 0],
    'shame': [0, 0, 0],        
    'fear': [0, 0, 1],
    'disgust': [1, 0, 0],
    'anger': [0, 1, 1],
    'enjoyment': [1, 0, 1],
    'startle': [1, 1, 0],
    'excitement': [1, 1, 1],
}

def compute_distances(row, key):
    # print(row['ser'])
    vector = [row['ser'], row['nor'], row['dop']]
    dist = distance.euclidean(MAPPING[key], vector)
    return dist

for key in MAPPING:
    df[key+'_distance'] = df.apply(lambda row: compute_distances(row, key), axis=1)



# sort and file writing

emotions = {
    'distress': 'страдание/тоска',
    'shame': 'стыд/унижение',        
    'fear': 'страх/ужас',
    'disgust': 'брезшливость/отвращение',
    'anger': 'злость/гнев',
    'enjoyment': 'удовольствие/радость',
    'startle': 'удивление',
    'excitement': 'интерес/возбуждение',
}

f = open('first_8_per_emotion.txt', 'w')

for key in MAPPING:
    df.sort_values([key+'_distance'], ascending=True, inplace=True)
    f.write("Первые 8 текстов для эмоции "+emotions[key]+": \n")
    for i in range (8):
        f.write(str(i+1)+". "+df.iloc[i]['text']+"\n")
    f.write("\n----------------------------------------\n\n")

f.close()