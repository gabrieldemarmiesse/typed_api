# typedapi

Typedapi is used when you want to gradually add types hints to your public API and you want to 
be able to track you progress and what's left to do.

With this, you enforce a TODO list of functions/classes to type (read exception list), 
and this list will always be up to date.

It's also helpful when contributors want to help and don't know what is left to do.

See https://github.com/tensorflow/addons/issues/989 for an application of this method.


Example:
 
```python
from types import ModuleType

from typedapi import ensure_api_is_typed

import tensorflow_addons

TUTORIAL_URL = "https://docs.python.org/3/library/typing.html"
HELP_MESSAGE = (
    "You can also take a look at the section about it in the CONTRIBUTING.md:\n"
    "https://github.com/tensorflow/addons/blob/master/CONTRIBUTING.md#about-type-hints"
)

# TODO: add types and remove all elements from
# the exception list.
EXCEPTION_LIST = [
    tensorflow_addons.losses.lifted_struct_loss,
    tensorflow_addons.losses.triplet_semihard_loss,
    tensorflow_addons.losses.LiftedStructLoss,
    tensorflow_addons.losses.TripletSemiHardLoss,
    tensorflow_addons.losses.npairs_loss,
    tensorflow_addons.losses.NpairsLoss,
    tensorflow_addons.losses.npairs_multilabel_loss,
    tensorflow_addons.losses.NpairsMultilabelLoss,
    tensorflow_addons.text.crf_binary_score,
    tensorflow_addons.text.crf_decode,
    tensorflow_addons.text.crf_decode_backward,
    tensorflow_addons.text.crf_decode_forward,
    tensorflow_addons.text.crf_forward,
    tensorflow_addons.text.crf_log_likelihood,
    tensorflow_addons.text.crf_log_norm,
    tensorflow_addons.text.crf_multitag_sequence_score,
    tensorflow_addons.text.crf_sequence_score,
    tensorflow_addons.text.crf_unary_score,
    tensorflow_addons.text.viterbi_decode,
    tensorflow_addons.text.skip_gram_sample,
    tensorflow_addons.text.skip_gram_sample_with_text_vocab,
    tensorflow_addons.text.parse_time,
]

modules_list = [
    tensorflow_addons.losses,
    tensorflow_addons.text,
    tensorflow_addons.image,
    tensorflow_addons.layers
]

if __name__ == "__main__":
    ensure_api_is_typed(
        modules_list, EXCEPTION_LIST, init_only=True, additional_message=HELP_MESSAGE,
    )
```


Licence: MIT
