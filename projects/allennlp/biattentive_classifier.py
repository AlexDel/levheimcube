from typing import Dict

import torch
from allennlp.models import Model
from allennlp.data import Vocabulary
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.token_embedders import Embedding


EMBEDDING_DIM = 512
HIDDEN_DIM = 256
EMBEDDING_DROPOUT = 0.2

class BiattentiveClassifier(Model):
    def __init__(
        self,
        vocab: Vocabulary,
        **kwargs
    ) -> None:
        super().__init__(vocab, **kwargs)

        self._text_field_embedder = BasicTextFieldEmbedder(
            {'tokens': Embedding(
                num_embeddings=self.vocab.get_vocab_size('tokens'), embedding_dim=EMBEDDING_DIM)
            })
        self._embedding_dropout = torch.nn.Dropout(EMBEDDING_DROPOUT)



