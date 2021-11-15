import torch
from transformers import AutoTokenizer

from projects.regression.regression_lightning import BERT,MAX_LENGTH, RegressionBert, outpul_cols


CHECKPOINT = 'https://storage.yandexcloud.net/nlp-dataset-bucket-1/models/regression-bert-val_loss%3D1.8566.ckpt'

model = RegressionBert.load_from_checkpoint(CHECKPOINT)
tokenizer = AutoTokenizer.from_pretrained(BERT)

def predict_diagonal_values(text):
    tokens = tokenizer.encode(text, padding='max_length', add_special_tokens=True, max_length=MAX_LENGTH, truncation=True)
    tokens = torch.tensor(tokens)

    prediction = torch.round(model(torch.unsqueeze(tokens, 0)))[0].tolist()
    prediction = dict(zip(outpul_cols, prediction))

    return prediction
