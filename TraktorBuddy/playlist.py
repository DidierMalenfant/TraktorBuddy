# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import xml.etree.ElementTree as ET

from typing import List
from .track import Track
from .tracklist import TrackList


# -- Class
class Playlist:
    """Interface for Traktor playlists."""

    def __init__(self, track_list: TrackList, node_element: ET.Element):
        """Constructor from an XML entry element."""

        self._node_element: ET.Element = node_element
        self._track_list: TrackList = track_list
        self._tracks: List[Track] = None

    def name(self) -> str:
        return self._node_element.get('NAME')

    def tracks(self) -> List[Track]:
        if self._tracks is not None:
            return self._tracks

        self._tracks = []

        playlist: Playlist = self._node_element.find('PLAYLIST')
        if playlist is None:
            return self._tracks

        if playlist.get('TYPE') != 'LIST':
            return self._tracks

        for entry in playlist.findall('ENTRY'):
            primary_key: ET.Element = entry.find('PRIMARYKEY')
            if primary_key is None or primary_key.get('TYPE') != 'TRACK':
                continue

            key: str = primary_key.get('KEY')
            if key is None:
                continue

            track: Track = self._track_list.trackWithPlaylistKey(key)
            if track is not None:
                self._tracks.append(track)

        return self._tracks
