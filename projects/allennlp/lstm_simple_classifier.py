from typing import Dict

import torch
from allennlp.data.iterators import BucketIterator
from allennlp.common.file_utils import cached_path
from allennlp.models import Model
from allennlp.modules.token_embedders import Embedding
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.seq2vec_encoders import PytorchSeq2VecWrapper
from allennlp.data.vocabulary import Vocabulary
from allennlp.training.metrics import CategoricalAccuracy, FBetaMeasure
from allennlp.training.trainer import Trainer
from allennlp.nn.util import get_text_field_mask
from allennlp.data.tokenizers.word_tokenizer import WordTokenizer

from projects.allennlp.tools.vk_data_loader import VkOverhearDatasetReader


EMBEDDING_DIM = 512
HIDDEN_DIM = 256

class VkOverhearEmotionClassifier(Model):
  def __init__(self, vocab: Vocabulary ):
    super().__init__(vocab)

    self.embedder = BasicTextFieldEmbedder({'tokens': Embedding(num_embeddings=vocab.get_vocab_size('tokens'), embedding_dim=EMBEDDING_DIM)})
    self.encoder = PytorchSeq2VecWrapper(torch.nn.LSTM(EMBEDDING_DIM, HIDDEN_DIM, batch_first=True))

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
    fmetrics = self.fbeta.get_metric(reset)
    return {
        'accuracy': self.accuracy.get_metric(reset),
        'fbeta': fmetrics['fscore']
      }


def main():
    cuda_device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    tokenizer = WordTokenizer()

    reader = VkOverhearDatasetReader(tokenizer)

    test_dataset = reader.read(cached_path(
        'https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.test.csv'))
    train_dataset = reader.read(cached_path(
        'https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.train.csv'))

    vocab = Vocabulary.from_instances(train_dataset + test_dataset)

    model = VkOverhearEmotionClassifier(vocab)
    model = model.cuda(cuda_device)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4, weight_decay=1e-5)

    iterator = BucketIterator(batch_size=4, sorting_keys=[("tokens", "num_tokens")])
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

main()
