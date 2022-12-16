# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

from enum import IntEnum, unique


@unique
class Color(IntEnum):
    Red = 1
    Orange = 2
    Yellow = 3
    Green = 4
    Blue = 5
    Violet = 6
    Magenta = 7
