from typing import Iterator, List, Dict

import torch
import pandas as pd

from allennlp.data import Instance
from allennlp.data.tokenizers import Token
from allennlp.data.tokenizers.tokenizer import Tokenizer
from allennlp.data.tokenizers.word_tokenizer import WordTokenizer
from allennlp.data.dataset_readers import DatasetReader
from allennlp.data.fields import TextField, LabelField
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.iterators import BucketIterator
from allennlp.common.file_utils import cached_path
from allennlp.models import Model
from allennlp.modules.text_field_embedders import TextFieldEmbedder, BasicTextFieldEmbedder
from allennlp.modules.token_embedders import Embedding
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.seq2vec_encoders import PytorchSeq2VecWrapper
from allennlp.modules.seq2vec_encoders import Seq2VecEncoder
from allennlp.data.vocabulary import Vocabulary
from allennlp.training.metrics import CategoricalAccuracy, FBetaMeasure
from allennlp.training.trainer import Trainer
from allennlp.nn.util import get_text_field_mask


EMBEDDING_DIM = 512
HIDDEN_DIM = 1024




class VkOverhearDatasetReader(DatasetReader):
  def __init__(self, tokenizer: Tokenizer = None):
    super().__init__(lazy=False)

    self.tokenizer = tokenizer or WordTokenizer()
    self.token_indexers = {"tokens": SingleIdTokenIndexer()}

  def text_to_instance(self, tokens: List[Token], emotion_label: str) -> Instance:
    fields = {}
    fields['tokens'] = TextField(tokens, self.token_indexers)
    fields['label'] = LabelField(emotion_label)

    return Instance(fields)

  def _read(self, file_path: str) -> Iterator[Instance]:
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
      tokens = self.tokenizer.tokenize(row['text'])
      label = row['emotion']
      yield self.text_to_instance(tokens, label)


reader = VkOverhearDatasetReader()

test_dataset = reader.read(cached_path('https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.test.csv'))
train_dataset = reader.read(cached_path('https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.train.csv'))






class VkOverhearEmotionClassifier(Model):
  def __init__(self,
               encoder: Seq2VecEncoder,
               embedder: TextFieldEmbedder,
               vocab: Vocabulary
    ):
    super().__init__(vocab)

    self.embedder = embedder
    self.encoder = encoder

    self.linear = torch.nn.Linear(in_features=self.encoder.get_output_dim(), out_features=self.vocab.get_vocab_size('labels'))

    self.accuracy = CategoricalAccuracy()
    self.fbeta = FBetaMeasure(average='macro')
    self.loss_fn = torch.nn.CrossEntropyLoss()


  def forward(self, tokens: Dict[str, torch.Tensor], label: torch.Tensor = None):

    mask = get_text_field_mask(tokens)

    embeddings = self.embedder(tokens)
    encoder_out = self.encoder(embeddings, mask)
    logits = self.linear(encoder_out)

    self.accuracy(logits, label)
    self.fbeta(logits, label)

    output = {
        'logits': logits,
        'loss': self.loss_fn(logits, label)
    }

    return output


  def get_metrics(self, reset = False):
    precision, recall, f1_measure = self.fbeta.get_metric(reset)
    print(f1_measure)
    return {
        'accuracy': self.accuracy.get_metric(reset),
        'fbeta': str(f1_measure)
      }


def main():
    cuda_device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    tokenizer = WordTokenizer()

    vocab = Vocabulary.from_instances(train_dataset + test_dataset)

    encoder = PytorchSeq2VecWrapper(torch.nn.LSTM(EMBEDDING_DIM, HIDDEN_DIM, batch_first=True))

    token_embeddings = Embedding(num_embeddings=vocab.get_vocab_size('tokens'), embedding_dim=EMBEDDING_DIM)
    word_embeddings = BasicTextFieldEmbedder({'tokens': token_embeddings})

    model = VkOverhearEmotionClassifier(encoder, word_embeddings, vocab)
    model = model.cuda(cuda_device)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4, weight_decay=1e-5)

    iterator = BucketIterator(batch_size=32, sorting_keys=[("tokens", "num_tokens")])
    iterator.index_with(vocab)

    trainer = Trainer(model=model,
                      optimizer=optimizer,
                      iterator=iterator,
                      train_dataset=train_dataset,
                      validation_dataset=test_dataset,
                      cuda_device=cuda_device,
                      patience=10,
                      num_epochs=20)
    trainer.train()