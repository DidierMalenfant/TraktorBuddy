# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

from enum import IntEnum, unique


@unique
class OpenNotation(IntEnum):
    Key_1d = 0    # -- C
    Key_8d = 1    # -- CsDb
    Key_3d = 2    # -- D
    Key_10d = 3   # -- DsEb
    Key_5d = 4    # -- E
    Key_12d = 5   # -- F
    Key_7d = 6    # -- FsGb
    Key_2d = 7    # -- G
    Key_9d = 8    # -- GsAb
    Key_4d = 9    # -- A
    Key_11d = 10  # -- AsBb
    Key_6d = 11   # -- B
    Key_10m = 12  # -- Cm
    Key_5m = 13   # -- CsmDbm
    Key_12m = 14  # -- Dm
    Key_7m = 15   # -- DsmEbm
    Key_2m = 16   # -- Em
    Key_9m = 17   # -- Fm
    Key_4m = 18   # -- FsmGbm
    Key_11m = 19  # -- Gm
    Key_6m = 20   # -- GsmAbm
    Key_1m = 21   # -- Am
    Key_8m = 22   # -- AsmBbm
    Key_3m = 23   # -- Bm
