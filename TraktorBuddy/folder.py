# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import xml.etree.ElementTree as ET

from typing import List
from .tracklist import TrackList
from .playlist import Playlist


# -- Class
class Folder:
    """Interface for Traktor folders."""

    def __init__(self, track_list: TrackList, node_element: ET.Element):
        """Constructor from an XML entry element."""

        self._node_element: ET.Element = node_element
        self._track_list: TrackList = track_list
        self._folders: List[Folder] = None
        self._playlists: List[Playlist] = None

    def name(self) -> str:
        return self._node_element.get('NAME')

    def find(self, names: List[str]):
        name: str = names[0]
        nb_of_names: int = len(names)

        for playlist in self.playlists():
            if playlist.name() == name:
                if nb_of_names == 1:
                    return playlist

        for folder in self.folders():
            if folder.name() == name:
                if nb_of_names == 1:
                    return folder
                else:
                    return folder.find(names[1:])

        return None

    def findFolder(self, names: List[str]):
        result = self.find(names)
        if type(result) != Folder:
            return None

        return result

    def findPlaylist(self, names: List[str]):
        result = self.find(names)
        if type(result) != Playlist:
            return None

        return result

    def folders(self) -> List['Folder']:
        if self._folders is not None:
            return self._folders

        self._folders = []

        subnodes: ET.Element = self._node_element.find('SUBNODES')
        if subnodes is None:
            return self._folders

        for node in subnodes.findall('NODE'):
            if node.get('TYPE') != 'FOLDER':
                continue

            self._folders.append(Folder(self._track_list, node))

        return self._folders

    def playlists(self) -> List[Playlist]:
        if self._playlists is not None:
            return self._playlists

        self._playlists = []

        subnodes: ET.Element = self._node_element.find('SUBNODES')
        if subnodes is None:
            return self._playlists

        for node in subnodes.findall('NODE'):
            if node.get('TYPE') != 'PLAYLIST':
                continue

            self._playlists.append(Playlist(self._track_list, node))

        return self._playlists
