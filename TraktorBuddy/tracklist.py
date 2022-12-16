# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import xml.etree.ElementTree as ET

from typing import List
from .track import Track


# -- Class
class TrackList:
    """Interface for Traktor track list inside a collection."""

    def __init__(self, collection_element: ET.Element):
        """Constructor from an XML collection element."""

        self._collection_element = collection_element
        self._tracks = None

    def tracks(self) -> List[Track]:
        if self._collection_element is None:
            return []

        if self._tracks is not None:
            return self._tracks

        self._tracks = []

        for entry in self._collection_element.findall('ENTRY'):
            track = Track(entry)
            if track.location() is not None:
                self._tracks.append(track)

        return self._tracks

    def trackWithPlaylistKey(self, key) -> Track:
        for track in self.tracks():
            if track._playlistKey() == key:
                return track

        return None
