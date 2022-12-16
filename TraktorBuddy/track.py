# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import xml.etree.ElementTree as ET

from datetime import datetime
from .utility import Utility
from .key import OpenNotation
from .rating import Rating
from .color import Color


# -- Class
class Track:
    """Interface for Traktor tracks."""

    def __init__(self, entry_element: ET.Element):
        """Constructor from an XML entry element."""

        self._entry_element: ET.Element = entry_element
        self._info_element: ET.Element = self._entry_element.find('INFO')
        self._album_element: ET.Element = self._entry_element.find('ALBUM')
        self._modified: bool = False

    def _entryElement(self) -> ET.Element:
        return self._entry_element

    def _getInfoElement(self) -> ET.Element:
        if self._info_element is None:
            self._info_element = ET.SubElement(self._entry_element, 'INFO')

        return self._info_element

    def _getFromInfoElement(self, key: str) -> str:
        if self._info_element is None:
            return None

        return self._info_element.get(key)

    def _getAlbumElement(self) -> ET.Element:
        if self._album_element is None:
            self._album_element = ET.SubElement(self._entry_element, 'ALBUM')

        return self._album_element

    def _getFromAlbumElement(self, key: str) -> str:
        if self._album_element is None:
            return None

        return self._album_element.get(key)

    def _setModifiedNow(self) -> None:
        if self._modified is True:
            return

        self._modified = True

        date = Utility.utcTimeNow()

        self._entry_element.set('MODIFIED_DATE', date.strftime('%Y/%m/%d'))
        self._entry_element.set('MODIFIED_TIME', str(date.second + (date.minute * 60) + (date.hour * 3600)))

    def _playlistKey(self) -> str:
        location = self._entry_element.find('LOCATION')

        if location is None:
            return None

        volume = location.get('VOLUME')

        if volume is None:
            return None

        directory = location.get('DIR')

        if directory is None:
            return None

        file = location.get('FILE')

        if file is None:
            return None

        return volume + directory + file

    def isASample(self) -> bool:
        return self._entry_element.find('LOOPINFO') is not None

    def location(self) -> str:
        playlist_key = self._playlistKey()
        if playlist_key is None:
            return None

        return '/Volumes/' + playlist_key.replace('/:', '/')

    def modificationDate(self) -> datetime:
        date = Utility.dateFromString(self._entry_element.get('MODIFIED_DATE'), '%Y/%m/%d')
        if date is None:
            return None

        seconds = Utility.stringToInt(self._entry_element.get('MODIFIED_TIME'))
        if seconds is None:
            return date

        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        # -- Traktor modification dates are stored in UTC time.
        return Utility.utcDatetime(date.year, date.month, date.day, hour, minutes, seconds)

    def title(self) -> str:
        return self._entry_element.get('TITLE')

    def setTitle(self, value) -> None:
        self._entry_element.set('TITLE', value)
        self._setModifiedNow()

    def artist(self) -> str:
        return self._entry_element.get('ARTIST')

    def setArtist(self, value) -> None:
        self._entry_element.set('ARTIST', value)
        self._setModifiedNow()

    def beatgridLocked(self) -> bool:
        return self._entry_element.get('LOCK') == '1'

    def setBeatGridLocked(self, value: bool) -> None:
        if value is True:
            string = '1'
        else:
            string = '0'

        self._entry_element.set('LOCK', string)
        self._setModifiedNow()

        date = Utility.utcTimeNow()
        self._entry_element.set('LOCK_MODIFICATION_TIME', date.strftime('%Y-%m-%dT%H:%M:%S'))

    def beatgridLockModifiedDate(self) -> datetime:
        string = self._entry_element.get('LOCK_MODIFICATION_TIME')
        if string is None:
            return None

        return Utility.dateFromString(string, '%Y-%m-%dT%H:%M:%S', utc=True)

    def bitrate(self) -> int:
        return Utility.stringToInt(self._getFromInfoElement('BITRATE'))

    def setBitrate(self, value: int) -> None:
        self._getInfoElement().set('BITRATE', str(value))
        self._setModifiedNow()

    def genre(self) -> str:
        return self._getFromInfoElement('GENRE')

    def setGenre(self, value: str) -> None:
        self._getInfoElement().set('GENRE', value)
        self._setModifiedNow()

    def label(self) -> str:
        return self._getFromInfoElement('LABEL')

    def setLabel(self, value: str) -> None:
        self._getInfoElement().set('LABEL', value)
        self._setModifiedNow()

    def producer(self) -> str:
        return self._getFromInfoElement('PRODUCER')

    def setProducer(self, value: str) -> None:
        self._getInfoElement().set('PRODUCER', value)
        self._setModifiedNow()

    def mix(self) -> str:
        return self._getFromInfoElement('MIX')

    def setMix(self, value: str) -> None:
        self._getInfoElement().set('MIX', value)
        self._setModifiedNow()

    def release(self) -> str:
        return self._getFromAlbumElement('TITLE')

    def setRelease(self, value: str) -> None:
        self._getAlbumElement().set('TITLE', value)
        self._setModifiedNow()

    def trackNumber(self) -> int:
        return Utility.stringToInt(self._getFromAlbumElement('TRACK'))

    def setTrackNumber(self, value: int) -> None:
        self._getAlbumElement().set('TRACK', str(value))
        self._setModifiedNow()

    def comments(self) -> str:
        return self._getFromInfoElement('COMMENT')

    def setComments(self, value: str) -> None:
        self._getInfoElement().set('COMMENT', value)
        self._setModifiedNow()

    def comments2(self) -> str:
        return self._getFromInfoElement('RATING')

    def setComments2(self, value: str) -> None:
        self._getInfoElement().set('RATING', value)
        self._setModifiedNow()

    def remixer(self) -> str:
        return self._getFromInfoElement('REMIXER')

    def setRemixer(self, value: str) -> None:
        self._getInfoElement().set('REMIXER', value)
        self._setModifiedNow()

    def key(self) -> str:
        return self._getFromInfoElement('KEY')

    def setKey(self, value: str) -> None:
        self._getInfoElement().set('KEY', value)
        self._setModifiedNow()

    def playCount(self) -> int:
        return Utility.stringToInt(self._getFromInfoElement('PLAYCOUNT'))

    def setPlayCount(self, value: int) -> None:
        self._getInfoElement().set('PLAYCOUNT', str(value))
        self._setModifiedNow()

    def length(self) -> float:
        return Utility.stringToFloat(self._getFromInfoElement('PLAYTIME_FLOAT'))

    def setLength(self, value: float) -> None:
        self._getInfoElement().set('PLAYTIME', str(round(value)))
        self._getInfoElement().set('PLAYTIME_FLOAT', '{:.06f}'.format(value))
        self._setModifiedNow()

    def rating(self) -> Rating:
        # -- The following works with rekordbox and Serato too:
        # --    Unrated -> 0, 1-51 -> 1, 52-102 -> 2, 103-153 -> 3, 154-204 -> 4, 205-anything -> 5
        value = Utility.stringToInt(self._getFromInfoElement('RANKING'))

        if value is None:
            return None

        if value == 0:
            return Rating.Unrated
        elif value < 52:
            return Rating.OneStar
        elif value < 103:
            return Rating.TwoStars
        elif value < 154:
            return Rating.ThreeStars
        elif value < 205:
            return Rating.FourStars
        elif value <= 255:
            return Rating.FiveStars

        return None

    def setRating(self, value: Rating) -> None:
        map = {
            Rating.Unrated: 0,
            Rating.OneStar: 51,
            Rating.TwoStars: 102,
            Rating.ThreeStars: 153,
            Rating.FourStars: 205,
            Rating.FiveStars: 255
        }

        self._getInfoElement().set('RANKING', str(map[value]))
        self._setModifiedNow()

    def importDate(self) -> datetime:
        return Utility.dateFromString(self._getFromInfoElement('IMPORT_DATE'), '%Y/%m/%d')

    def setImportDate(self, value: datetime) -> None:
        self._getInfoElement().set('IMPORT_DATE', value.strftime('%Y/%m/%d'))
        self._setModifiedNow()

    def lastPlayedDate(self) -> datetime:
        return Utility.dateFromString(self._getFromInfoElement('LAST_PLAYED'), '%Y/%m/%d')

    def setLastPlayedDate(self, value: datetime) -> None:
        self._getInfoElement().set('LAST_PLAYED', value.strftime('%Y/%m/%d'))
        self._setModifiedNow()

    def releaseDate(self) -> datetime:
        return Utility.dateFromString(self._getFromInfoElement('RELEASE_DATE'), '%Y/%m/%d')

    def setReleaseDate(self, value: datetime) -> None:
        self._getInfoElement().set('RELEASE_DATE', value.strftime('%Y/%m/%d'))
        self._setModifiedNow()

    def fileSize(self) -> int:
        return Utility.stringToInt(self._getFromInfoElement('FILESIZE'))

    def setFileSize(self, value: int) -> None:
        self._getInfoElement().set('FILESIZE', str(value))
        self._setModifiedNow()

    def bpm(self) -> float:
        tempo_element = self._entry_element.find('TEMPO')
        if tempo_element is None:
            return None

        return Utility.stringToFloat(tempo_element.get('BPM'))

    def setBpm(self, value: float) -> None:
        tempo_element = self._entry_element.find('TEMPO')
        if tempo_element is None:
            tempo_element = ET.SubElement(self._entry_element, 'TEMPO')

        tempo_element.set('BPM', '{:.06f}'.format(value))
        tempo_element.set('BPM_QUALITY', '100.000000')
        self._setModifiedNow()

    def traktorKey(self) -> OpenNotation:
        key_element = self._entry_element.find('MUSICAL_KEY')
        if key_element is None:
            return None

        value = Utility.stringToInt(key_element.get('VALUE'))
        if value is None:
            return None

        try:
            result = OpenNotation(value)
        except ValueError:
            return None

        return result

    def setTraktorKey(self, value: OpenNotation) -> None:
        key_element = self._entry_element.find('MUSICAL_KEY')
        if key_element is None:
            key_element = ET.SubElement(self._entry_element, 'MUSICAL_KEY')

        key_element.set('VALUE', str(int(value)))
        self._setModifiedNow()

    def color(self) -> Color:
        value = Utility.stringToInt(self._getFromInfoElement('COLOR'))

        if value is None:
            return None

        try:
            result = Color(value)
        except ValueError:
            return None

        return result

    def setColor(self, value: Color) -> None:
        self._getInfoElement().set('COLOR', str(int(value)))
        self._setModifiedNow()
