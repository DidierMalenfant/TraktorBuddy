# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import pytz

import xml.etree.ElementTree as ET

from datetime import datetime


# -- Class
class Utility:
    """Helper methods."""

    # -- This is used in Unit tests to mock the time for 'now'.
    _mock_now_date = None

    @classmethod
    def stringToInt(cls, string: str) -> int:
        if string is None:
            return None

        return int(string)

    @classmethod
    def stringToFloat(cls, string: str) -> float:
        if string is None:
            return None

        return float(string)

    @classmethod
    def dateFromString(cls, string: str, format: str, utc: bool = False) -> datetime:
        if string is None:
            return None

        try:
            date = datetime.strptime(string, format)
            if utc:
                date = pytz.utc.localize(date)

            return date
        except ValueError:
            return None

    @classmethod
    def utcTimeNow(cls) -> datetime:
        if Utility._mock_now_date is not None:
            return Utility._mock_now_date

        return datetime.now().astimezone(pytz.utc)

    @classmethod
    def utcDatetime(cls, year: int, month: int, day: int, hour: int, minutes: int, seconds: int) -> datetime:
        return pytz.utc.localize(datetime(year, month, day, hour, minutes, seconds))

    @classmethod
    def xmlElementToString(cls, element: ET.Element, xml_declaration: bool = False) -> str:
        return ET.tostring(element, encoding='unicode', short_empty_elements=False, xml_declaration=xml_declaration)
