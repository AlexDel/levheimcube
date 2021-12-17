import torch
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import AutoTokenizer

from projects.regression.regression_lightning import BERT,MAX_LENGTH, RegressionBert, outpul_cols


CHECKPOINT = 'https://storage.yandexcloud.net/nlp-dataset-bucket-1/models/regression-bert-val_loss%3D1.784316.ckpt'

model = RegressionBert.load_from_checkpoint(CHECKPOINT)
tokenizer = AutoTokenizer.from_pretrained(BERT)

def predict_diagonal_values(text, model, tokenizer):
    tokens = tokenizer.encode(text, padding='max_length', add_special_tokens=True, max_length=MAX_LENGTH, truncation=True)
    tokens = torch.tensor(tokens)

    prediction = model(torch.unsqueeze(tokens, 0))[0].tolist()
    prediction = dict(zip(map(lambda x: x.split(':')[1], outpul_cols), prediction))

    return prediction

app = FastAPI()


class Req(BaseModel):
    text: str
    key: str

@app.post("/predict")
def predict(req: Req):
    if req.key != 'lcube':
        return {}

    prediction = predict_diagonal_values(req.text, model, tokenizer)
    response = jsonable_encoder(prediction)

    return JSONResponse(content=response)


app.mount("/", StaticFiles(directory="static",html = True), name="static")
