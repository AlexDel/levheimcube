import pandas as pd
import torch.utils.data as Data
from torch.optim.lr_scheduler import StepLR
import torch
from transformers import AutoModel, AutoTokenizer
from torch.utils.data import Dataset
import argparse
import os
import copy
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from math import sqrt
from tqdm.notebook import tqdm
from datetime import datetime

EPOCHS = 10
SEED = 2021
BERT = 'DeepPavlov/rubert-base-cased'
MAX_LENGTH = 200
BATCH_SIZE = 8

input_col = 'INPUT:text'
outpul_cols = ['OUTPUT:disgust_rage', 'OUTPUT:fear_surprise', 'OUTPUT:shame_excitement', 'OUTPUT:enjoyment_distress']
data_url = "https://storage.yandexcloud.net/nlp-dataset-bucket-1/toloka-vk-proceedings-2020/toloka-vk-raw-unprocessed.tsv"

class OverhearRegressionDataset(Dataset):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(BERT)

        df = pd.read_csv(data_url, sep='\t', usecols=[input_col, *outpul_cols], index_col=False, header=0)
        df = df.dropna(how='all')
        self.df = df

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, index):
        row = self.df.iloc[[index]]
        text = row[input_col].values[0]
        diagonal_values = row[outpul_cols].values[0]

        embeddings = self.tokenizer.encode(text, padding='max_length', max_length=MAX_LENGTH, truncation=True)

        x = torch.tensor(embeddings)
        y = torch.tensor(diagonal_values, dtype=torch.float)
        return x, y


class RegressionBert(torch.nn.Module):
    def __init__(self, freeze_bert=True):
        super(RegressionBert, self).__init__()
        self.bert = AutoModel.from_pretrained(BERT, num_labels=1)
        if freeze_bert:
            for p in self.bert.parameters():
                p.requires_grad = False
        self.fc0 = torch.nn.Linear(768, 2048)
        self.fc1 = torch.nn.Linear(2048, 512)
        self.fc2 = torch.nn.Linear(512, 128)
        self.fc3 = torch.nn.Linear(128, 4)

    def forward(self, x, att=None):
        x = self.bert(x, attention_mask=att)[0]
        x = x[:, 0, :]
        x = self.fc0(x)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = RegressionBert().to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
f_loss = torch.nn.MSELoss()

dataset = OverhearRegressionDataset()
dataloader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)

for epoch in range(EPOCHS):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(dataloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, values = data
        inputs = inputs.to(device)
        values = values.to(device)

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = model(inputs)
        loss = f_loss(outputs, values)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 100 == 99:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 100))
            running_loss = 0.0

print('Finished Training')