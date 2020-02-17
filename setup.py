# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""TensorFlow Addons.

TensorFlow Addons is a repository of contributions that conform to well-
established API patterns, but implement new functionality not available
in core TensorFlow. TensorFlow natively supports a large number of
operators, layers, metrics, losses, and optimizers. However, in a fast
moving field like ML, there are many interesting new developments that
cannot be integrated into core TensorFlow (because their broad
applicability is not yet clear, or it is mostly used by a smaller subset
of the community).
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name="typedapi",
    version="0.2.0",
    author="Gabriel de Marmiesse",
    author_email="gabrieldemarmiesse@gmail.com",
    packages=find_packages(),
)
