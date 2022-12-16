# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import os
import shutil

import xml.etree.ElementTree as ET

from typing import List
from semver import VersionInfo
from time import sleep
from .utility import Utility
from .track import Track
from .tracklist import TrackList
from .folder import Folder


# -- Classes
class Collection:
    """Interface for Traktor collection."""

    def __init__(self, collection_path: str = None, _mock_element: ET.Element = None):
        """Constructor from a collection path, or it will just use the latest collection if no path is provided."""

        self._nml_element = None

        if _mock_element is None:
            if collection_path is None:
                self._collection_path = Collection.latestTraktorFolderPath()

                if self._collection_path is None:
                    raise RuntimeError('Error: Could not find any Traktor folder in \'' + Collection.nativeInstrumentsFolderPath() + '\'.')
            else:
                self._collection_path = collection_path

            print('Parsing Traktor collection in \'' + self._collection_path + '\'.')

            self._nml_element = ET.ElementTree(file=self._collection_path).getroot()
        else:
            self._nml_element = _mock_element

        self._track_list = TrackList(self._nml_element.find('COLLECTION'))

    def makeBackup(self):
        # -- Backups filename have a timestamp so we make sure to wait so that names cannot clash.
        sleep(1)

        backup_folder = Collection.traktorCollectionBabkupFolderPath()
        os.makedirs(backup_folder, exist_ok=True)

        backup_destination = os.path.join(backup_folder, Utility.utcTimeNow().strftime('%Y-%m-%d-%H-%M-%S.nml'))
        shutil.copy(self._collection_path, backup_destination)

    def save(self):
        self.makeBackup()

        with open(self._collection_path, 'w') as out_file:
            out_file.write(Utility.xmlElementToString(self._nml_element, xml_declaration=True))

        print('Saved Traktor collection in \'' + self._collection_path + '\'.')

    def tracks(self) -> List[Track]:
        return self._track_list.tracks()

    def rootFolder(self) -> Folder:
        playlists_element: ET.Element = self._nml_element.find('PLAYLISTS')
        if playlists_element is None:
            return None

        root_node: ET.Element = playlists_element.find('NODE')
        if root_node is None:
            return None

        return Folder(self._track_list, root_node)

    def trackWithPlaylistKey(self, key) -> Track:
        return self._track_list.trackWithPlaylistKey(key)

    @classmethod
    def purgeBackups(cls, test_mode: bool = False):
        backup_folder: str = Collection.traktorCollectionBabkupFolderPath()
        backup_list: List[str] = os.listdir(backup_folder)

        nb_of_backups: int = len(backup_list)
        if nb_of_backups < 2:
            print('No backups to purge.')
            return

        if test_mode is False:
            backup_list.sort()

            for file in backup_list[:-1]:
                os.remove(os.path.join(backup_folder, file))

        print('Purged ' + str(nb_of_backups - 1) + ' backup(s).')

    @classmethod
    def traktorBuddyFolderPath(cls) -> str:
        return os.path.join(os.path.expanduser('~'), '.tktbud')

    @classmethod
    def traktorCollectionBabkupFolderPath(cls) -> str:
        return os.path.join(Collection.traktorBuddyFolderPath(), 'backups')

    @classmethod
    def nativeInstrumentsFolderPath(cls) -> str:
        return os.path.join(os.path.expanduser('~'), 'Documents', 'Native Instruments')

    @classmethod
    def latestTraktorFolderPath(cls) -> str:
        base_folder = Collection.nativeInstrumentsFolderPath()

        lastest_version = None

        for path in os.listdir(base_folder):
            if not path.startswith('Traktor '):
                continue

            try:
                version = VersionInfo.parse(path[8:])

                if lastest_version is None or version > lastest_version:
                    lastest_version = version
            except ValueError:
                continue

        if lastest_version is None:
            return None

        return os.path.join(base_folder, 'Traktor ' + str(lastest_version), 'collection.nml')
