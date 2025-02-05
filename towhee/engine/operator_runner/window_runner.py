# Copyright 2021 Zilliz. All rights reserved.
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

from typing import Tuple, Union, Dict, List
import traceback

from towhee.engine.operator_runner.map_runner import MapRunner
from towhee.engine.status import Status
from towhee.utils.log import engine_log


class WindowRunner(MapRunner):
    """
    WindowRunner, multiple inputs and multiple outputs.

    Wrapper will run in task executor in another thread or process.
    If run an op error, we should pass error info by an error handler.
    """

    def _set_outputs(self, output: List[any]):
        if not isinstance(output, list):
            raise RuntimeError("Window operator's output must be a list, not a {}".format(type(output)))

        for data in output:
            self._writer.write(data)

    def _call_op(self, inputs: List[Dict]) -> Tuple[bool, Union[str, any]]:
        try:
            outputs = self._op(inputs)
            return Status.ok_status(outputs)
        except Exception as e:  # pylint: disable=broad-except
            err = "{}, {}".format(e, traceback.format_exc())
            engine_log.error(err)
            return Status.err_status(err)
