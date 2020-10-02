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

from allennlp.common.checks import check_dimensions_match, ConfigurationError
from allennlp.data import TextFieldTensors, Vocabulary
from allennlp.modules import Elmo, FeedForward, Maxout, Seq2SeqEncoder, TextFieldEmbedder
from allennlp.models.model import Model
from allennlp.nn import InitializerApplicator
from allennlp.nn import util
from allennlp.training.metrics import CategoricalAccuracy

from projects.allennlp.tools.vk_data_loader import VkOverhearDatasetReader

