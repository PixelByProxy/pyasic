# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.backends import VNish
from pyasic.miners.device.models import S21, S21Hydro, S21Plus, S21PlusHydro, S21Pro


class VNishS21(VNish, S21):
    pass


class VNishS21Plus(VNish, S21Plus):
    pass


class VNishS21PlusHydro(VNish, S21PlusHydro):
    pass


class VNishS21Pro(VNish, S21Pro):
    pass


class VNishS21Hydro(VNish, S21Hydro):
    pass
