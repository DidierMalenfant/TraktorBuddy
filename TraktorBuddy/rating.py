# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

from enum import IntEnum, unique


@unique
class Rating(IntEnum):
    Unrated = 0
    OneStar = 1
    TwoStars = 2
    ThreeStars = 3
    FourStars = 4
    FiveStars = 5
