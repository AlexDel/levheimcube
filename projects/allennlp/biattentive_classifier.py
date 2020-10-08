import torch
from allennlp.models import Model
from allennlp.data import Vocabulary
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.token_embedders import Embedding
from allennlp.modules import FeedForward
from allennlp.modules.seq2seq_encoders import PytorchSeq2SeqWrapper
from allennlp.common.checks import check_dimensions_match


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

        self._num_classes = self.vocab.get_vocab_size('labels')

        self._pre_encode_feed_forward = FeedForward(input_dim=EMBEDDING_DIM, num_layers=1, activations=torch.nn.ReLU, hidden_dims=[HIDDEN_DIM])
        self._encoder  = PytorchSeq2SeqWrapper(torch.nn.LSTM(EMBEDDING_DIM, HIDDEN_DIM, batch_first=True))

        self._integrator = PytorchSeq2SeqWrapper(torch.nn.LSTM(EMBEDDING_DIM * 2, HIDDEN_DIM, batch_first=True))
        self._integrator_dropout = torch.nn.Dropout(EMBEDDING_DROPOUT)
        self._combined_integrator_output_dim = self._integrator.get_output_dim()

        self._self_attentive_pooling_projection = torch.nn.Linear(self._combined_integrator_output_dim, 1)

        self._output_layer = FeedForward(input_dim=HIDDEN_DIM * 4, num_layers=1, hidden_dims=self._num_classes, activations=torch.nn.ReLU)

        check_dimensions_match(
            self._text_field_embedder.get_output_dim(),
            self._pre_encode_feed_forward.get_input_dim(),
            "text field embedder output dim",
            "Pre-encoder feedforward input dim",
        )





