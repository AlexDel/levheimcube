import pandas as pd
import torch
from transformers import AutoModel, AutoTokenizer
from torch.utils.data import Dataset
import pytorch_lightning as pl
from torch.utils.data import random_split, DataLoader
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks import ModelCheckpoint

EPOCHS = 100
SEED = 2021
BERT = 'DeepPavlov/distilrubert-tiny-cased-conversational'
MAX_LENGTH = 200
BATCH_SIZE = 16

input_col = 'INPUT:text'
outpul_cols = ['OUTPUT:disgust_rage', 'OUTPUT:fear_surprise', 'OUTPUT:shame_excitement', 'OUTPUT:enjoyment_distress']
data_url = "https://storage.yandexcloud.net/nlp-dataset-bucket-1/toloka-vk-proceedings-2020/toloka-vk-raw-unprocessed.tsv"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

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

        tokens = self.tokenizer.encode(text, padding='max_length', add_special_tokens=True, max_length=MAX_LENGTH, truncation=True)

        x = torch.tensor(tokens)
        y = torch.tensor(diagonal_values, dtype=torch.float)
        return x, y


class RegressionBert(pl.LightningModule):
    def __init__(self, freeze_bert=False):
        super(RegressionBert, self).__init__()
        self.bert = AutoModel.from_pretrained(BERT, num_labels=1)
        if freeze_bert:
            for p in self.bert.parameters():
                p.requires_grad = False
        self.fc0 = torch.nn.Linear(768, 2048)
        self.fc1 = torch.nn.Linear(2048, 512)
        self.fc2 = torch.nn.Linear(512, 128)
        self.fc3 = torch.nn.Linear(128, 4)

        self.lrelu = torch.nn.LeakyReLU()

        self.train_loss = torch.nn.MSELoss()
        self.val_loss = torch.nn.L1Loss()

    def forward(self, x, att=None):
        x = self.bert(x, attention_mask=att)[0]
        x = torch.mean(x, dim=1)
        x = self.lrelu(self.fc0(x))
        x = self.lrelu(self.fc1(x))
        x = self.lrelu(self.fc2(x))
        x = self.fc3(x)
        return x

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=0.001)
        return optimizer

    def training_step(self, train_batch, batch_idx):
        inputs, values = train_batch
        outputs = self.forward(inputs)
        loss = self.train_loss(outputs, values)
        self.log('train_loss', loss)

        return loss

    def validation_step(self, train_batch, batch_idx):
        inputs, values = train_batch
        outputs = self.forward(inputs)
        loss = self.val_loss(outputs, values)
        self.log('val_loss', loss)

        return loss

dataset = OverhearRegressionDataset()
data_train, data_val = random_split(dataset, [3000, 965])

train_loader = DataLoader(data_train, batch_size=BATCH_SIZE)
val_loader = DataLoader(data_val, batch_size=BATCH_SIZE)

if __name__ == '__main__':
    model = RegressionBert()

    # training
    early_stopping = EarlyStopping(monitor="val_loss", min_delta=0.05, mode='min')
    checkpoint_callback = ModelCheckpoint(
        monitor="val_loss",
        dirpath="models",
        filename="regression-bert-{val_loss:.4f}",
        save_top_k=2,
        mode="min",
    )

    logger = TensorBoardLogger('logs')
    trainer = pl.Trainer(log_every_n_steps=15, logger=logger, callbacks=[checkpoint_callback])
    trainer.fit(model, train_loader, val_loader)