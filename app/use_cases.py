import torch
from transformers import AutoModel, AutoTokenizer

from projects.regression.regression_lightning import BERT, RegressionBert


CHECKPOINT = 'https://storage.yandexcloud.net/nlp-dataset-bucket-1/models/regression-bert-val_loss%3D1.8566.ckpt'

model = RegressionBert.load_from_checkpoint(CHECKPOINT)
tokenizer = AutoTokenizer.from_pretrained(BERT)

def predict_diagonal_values(text):
    tokens = tokenizer.encode(text, padding='max_length', add_special_tokens=True, max_length=MAX_LENGTH, truncation=True)
    tokens = torch.tensor(tokens)

    prediction = model(tokens)

    return prediction


#p = predict_diagonal_values('Работаю педиатром в инфекционном отделении. Поступает к нам мальчик с гастроэнтеритом (диарея, рвота). Один из главных вопросов: "Что ребёнок ел?" Мама: "Сейчас мы болеем, так что только грудь". Ребёнку 6 лет.')
