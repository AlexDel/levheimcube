from typing import Iterator, List, Dict

import pandas as pd
from allennlp.data import Instance
from allennlp.data.tokenizers import Token
from allennlp.data.tokenizers.tokenizer import Tokenizer
from allennlp.data.tokenizers.word_tokenizer import WordTokenizer
from allennlp.data.dataset_readers import DatasetReader
from allennlp.data.fields import TextField, LabelField
from allennlp.data.token_indexers import SingleIdTokenIndexer


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
