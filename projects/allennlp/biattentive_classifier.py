import torch
from allennlp.models import Model
from allennlp.data import Vocabulary
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.token_embedders import Embedding
from allennlp.modules import FeedForward
from allennlp.modules.seq2seq_encoders import PytorchSeq2SeqWrapper
from allennlp.common.checks import check_dimensions_match
from allennlp.training.metrics import CategoricalAccuracy
from allennlp.nn.util import get_text_field_mask
from allennlp.data.tokenizers import WordTokenizer
from allennlp.common.file_utils import cached_path

from projects.allennlp.tools.vk_data_loader import VkOverhearDatasetReader


EMBEDDING_DIM = 10
PRE_ENCODE_OUTPUT_DIM = 3
ENCODER_HIDDEN_DIM = 2
INTEGRATOR_HIDDEN_DIM = 3
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

        self._pre_encode_feed_forward = FeedForward(input_dim=EMBEDDING_DIM, num_layers=1, activations=torch.nn.ReLU, hidden_dims=[PRE_ENCODE_OUTPUT_DIM])
        self._encoder  = PytorchSeq2SeqWrapper(torch.nn.LSTM(PRE_ENCODE_OUTPUT_DIM, ENCODER_HIDDEN_DIM, batch_first=True))

        self._integrator = PytorchSeq2SeqWrapper(torch.nn.LSTM(PRE_ENCODE_OUTPUT_DIM * 2, INTEGRATOR_HIDDEN_DIM, batch_first=True))
        self._integrator_dropout = torch.nn.Dropout(EMBEDDING_DROPOUT)
        self._combined_integrator_output_dim = self._integrator.get_output_dim()

        self._self_attentive_pooling_projection = torch.nn.Linear(self._combined_integrator_output_dim, 1)

        self._output_layer = FeedForward(input_dim=INTEGRATOR_HIDDEN_DIM * 4, num_layers=1, hidden_dims=self._num_classes, activations=torch.nn.ReLU)

        check_dimensions_match(
            self._text_field_embedder.get_output_dim(),
            self._pre_encode_feed_forward.get_input_dim(),
            "text field embedder output dim",
            "Pre-encoder feedforward input dim",
        )

        check_dimensions_match(
            self._pre_encode_feed_forward.get_output_dim(),
            self._encoder.get_input_dim(),
            'Pre-encoder output dim',
            'LSTM encodeer input dim'
        )

        check_dimensions_match(
            self._encoder.get_output_dim() * 3,
            self._integrator.get_input_dim(),
            'LSTM encoder output dim * 2',
            'Integrator input dim'
        )

        check_dimensions_match(
            self._integrator.get_output_dim() * 4,
            self._output_layer.get_input_dim(),
             "Integrator output dim * 4",
             "Output layer input dim",
        )

        check_dimensions_match(
            self._output_layer.get_output_dim(),
            self._num_classes,
            "Output layer output dim",
            "Number of classes.",
        )

        self.metrics = {
            'accuracy': CategoricalAccuracy(),
            'accuracy3': CategoricalAccuracy(top_k=3)
        }

        self.loss = torch.nn.CrossEntropyLoss()


    def forward(self, tokens, label: torch.LongTensor = None):
        text_mask = get_text_field_mask(tokens)

        embedded_text = self._text_field_embedder(tokens)



def main():
    cuda_device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    tokenizer = WordTokenizer()

    reader = VkOverhearDatasetReader(tokenizer)

    test_dataset = reader.read(cached_path(
        'https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.test.csv'))
    train_dataset = reader.read(cached_path(
        'https://storage.yandexcloud.net/nlp-dataset-bucket-1/vk-hashtag-public-exports-2019/vk_overhear_without_neutral.train.csv'))

    vocab = Vocabulary.from_instances(train_dataset + test_dataset)

    model = BiattentiveClassifier(vocab)
    model = model.cuda(cuda_device)

    # optimizer = torch.optim.Adam(model.parameters(), lr=1e-4, weight_decay=1e-5)
    #
    # iterator = BucketIterator(batch_size=4, sorting_keys=[("tokens", "num_tokens")])
    # iterator.index_with(vocab)
    #
    # trainer = Trainer(model=model,
    #                   optimizer=optimizer,
    #                   iterator=iterator,
    #                   train_dataset=train_dataset,
    #                   validation_dataset=test_dataset,
    #                   cuda_device=cuda_device,
    #                   patience=10,
    #                   num_epochs=20)
    # trainer.train()

main()


