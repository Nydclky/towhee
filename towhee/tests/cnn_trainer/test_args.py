# coding=utf-8
# Copyright 2020-present the HuggingFace Inc. team and 2021 Zilliz.
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

import unittest

from towhee.cnn_trainer.training_args import TrainingArguments


class TrainerArgsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.training_args = TrainingArguments(
            output_dir='./ResNet50',
            overwrite_output_dir=True,
            num_train_epochs=5,
            per_gpu_train_batch_size=4,
            prediction_loss_only=True,
        )

    def test_train_batch_size(self) -> None:
        self.assertEqual(4, self.training_args.train_batch_size)


if __name__ == '__main__':
    unittest.main(verbosity=1)
