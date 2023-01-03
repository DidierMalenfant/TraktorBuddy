# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import getopt
import sys

from typing import List
from .__about__ import __version__
from .exceptions import ArgumentError
from .collection import Collection
from .track import Track
from .folder import Folder


# -- Classes
class TraktorBuddy:
    """A helping hand for managing Traktor collections."""

    def __init__(self, args):
        """Constructor based on command line arguments."""

        self._test_mode: bool = False
        self._all_tracks: bool = False

        try:
            # -- Gather the arguments
            opts, self._commands = getopt.getopt(args, 'hta', ['help', 'test', 'all'])

            for o, a in opts:
                if o in ('-h', '--help'):
                    self.printUsage()
                    sys.exit(0)
                elif o in ('-t', '--test'):
                    print('Running in test mode.')
                    self._test_mode = True
                elif o in ('-a', '--all'):
                    print('Applying command to all tracks.')
                    self._all_tracks = True

            if len(self._commands) == 0:
                raise ArgumentError('Expected a command! Maybe start with `tktbud --help`?')
        except getopt.GetoptError:
            self.printUsage()
            sys.exit(0)

    def main(self) -> None:
        switch = {
            'help': self.printUsage,
            'version': TraktorBuddy.printVersion,
            'tag': self.tag,
            'purge': self.purgeBackups
        }

        if self._commands is None:
            raise ArgumentError('Expected a command! Maybe start with `tktbud --help`?')
            return

        command = self._commands[0]
        method = switch.get(command)
        if method is None:
            raise ArgumentError('Unknown commanwd \'' + command + '\'.')

        method()

    def tag(self) -> None:
        if len(self._commands) < 2:
            raise ArgumentError('Expected an argument to \'tag\' command.')

        switch = {
            'add': self.addTag,
            'remove': self.removeTag,
            'rename': self.renameTag,
            'years': self.addYearTag
        }

        sub_command = self._commands[1]
        method = switch.get(sub_command)
        if method is None:
            raise ArgumentError('Unknown argument \'' + sub_command + '\' to \'tag\' command.')

        method()

    def addTag(self) -> None:
        nb_of_commands: int = len(self._commands)

        if nb_of_commands > 4:
            raise ArgumentError('Too many arguments to \'add\' command.')

        if nb_of_commands < 3:
            raise ArgumentError('Expected name argument to \'add\' command.')

        tag_name: str = self._commands[2]
        if tag_name.__contains__(' '):
            raise ArgumentError('Tag names should not contain spaces.')

        if self._all_tracks is True:
            if nb_of_commands > 3:
                raise ArgumentError('No need for path argument to \'add\' command when \'--all\' option is used.')
        elif nb_of_commands < 4:
            raise ArgumentError('Expected path argument to \'add\' command.')

        collection = Collection()
        if self._all_tracks is True:
            tracks = collection.tracks()
        else:
            tracks = TraktorBuddy.findAllTracksAtPath(collection, self._commands[3])

        nb_of_tracks_tagged: int = 0
        for track in tracks:
            if track.isASample():
                continue

            existing_value: str = track.comments2()
            if existing_value is None:
                existing_value = tag_name
            elif tag_name in existing_value.split(' '):
                continue
            else:
                existing_value += ' ' + tag_name

            track.setComments2(existing_value)
            nb_of_tracks_tagged += 1

            if self._test_mode is True:
                print(track.location())

        print('Tagged ' + str(nb_of_tracks_tagged) + ' tracks.')
        if self._test_mode is False and nb_of_tracks_tagged > 0:
            collection.save()

    def removeTag(self) -> None:
        nb_of_commands: int = len(self._commands)

        if nb_of_commands > 4:
            raise ArgumentError('Too many arguments to \'remove\' command.')

        if nb_of_commands < 3:
            raise ArgumentError('Expected name argument to \'remove\' command.')

        tag_name: str = self._commands[2]
        if tag_name.__contains__(' '):
            raise ArgumentError('Tag names should not contain spaces.')

        if self._all_tracks is True:
            if nb_of_commands > 3:
                raise ArgumentError('No need for path argument to \'remove\' command when \'--all\' option is used.')
        elif nb_of_commands < 4:
            raise ArgumentError('Expected path argument to \'remove\' command.')

        collection = Collection()
        if self._all_tracks is True:
            tracks = collection.tracks()
        else:
            tracks = TraktorBuddy.findAllTracksAtPath(collection, self._commands[3])

        nb_of_tracks_tagged: int = 0
        for track in tracks:
            if track.isASample():
                continue

            existing_value: str = track.comments2()
            if existing_value is None:
                continue

            names = existing_value.split(' ')
            if tag_name not in names:
                continue

            names.remove(tag_name)
            track.setComments2(" ".join(names))
            nb_of_tracks_tagged += 1

            if self._test_mode is True:
                print(track.location())

        print('Removed tag from ' + str(nb_of_tracks_tagged) + ' tracks.')
        if self._test_mode is False and nb_of_tracks_tagged > 0:
            collection.save()

    def renameTag(self) -> None:
        nb_of_commands: int = len(self._commands)

        if nb_of_commands > 5:
            raise ArgumentError('Too many arguments to \'rename\' command.')

        if nb_of_commands < 4:
            raise ArgumentError('Expected old and new name arguments to \'rename\' command.')

        old_tag_name: str = self._commands[2]
        if old_tag_name.__contains__(' '):
            raise ArgumentError('Tag names should not contain spaces.')

        new_tag_name: str = self._commands[3]
        if new_tag_name.__contains__(' '):
            raise ArgumentError('Tag names should not contain spaces.')

        if self._all_tracks is True:
            if nb_of_commands > 4:
                raise ArgumentError('No need for path argument to \'rename\' command when \'--all\' option is used.')
        elif nb_of_commands < 5:
            raise ArgumentError('Expected path argument to \'rename\' command.')

        collection = Collection()
        if self._all_tracks is True:
            tracks = collection.tracks()
        else:
            tracks = TraktorBuddy.findAllTracksAtPath(collection, self._commands[4])

        nb_of_tracks_tagged: int = 0
        for track in tracks:
            if track.isASample():
                continue

            existing_value: str = track.comments2()
            if existing_value is None:
                continue

            names = existing_value.split(' ')
            if old_tag_name not in names:
                continue

            names.remove(old_tag_name)
            track.setComments2(" ".join(names) + ' ' + new_tag_name)
            nb_of_tracks_tagged += 1

            if self._test_mode is True:
                print(track.location())

        print('Renamed tag in ' + str(nb_of_tracks_tagged) + ' tracks.')
        if self._test_mode is False and nb_of_tracks_tagged > 0:
            collection.save()

    def addYearTag(self) -> None:
        nb_of_commands: int = len(self._commands)
        print(nb_of_commands)

        if nb_of_commands > 3:
            raise ArgumentError('Too many arguments to \'years\' command.')

        if self._all_tracks is True:
            if nb_of_commands > 2:
                raise ArgumentError('No need for path argument to \'years\' command when \'--all\' option is used.')
        elif nb_of_commands < 3:
            raise ArgumentError('Expected path argument to \'years\' command.')

        collection = Collection()
        if self._all_tracks is True:
            tracks = collection.tracks()
        else:
            tracks = TraktorBuddy.findAllTracksAtPath(collection, self._commands[2])

        nb_of_tracks_tagged: int = 0
        for track in tracks:
            if track.isASample():
                continue

            release_date = track.releaseDate()
            if release_date is None:
                continue

            year: int = track.releaseDate().year
            if year == 0:
                continue

            tag_name: str = 'Year:' + str(year)

            existing_value: str = track.comments2()
            if existing_value is None:
                existing_value = tag_name
            elif tag_name in existing_value.split(' '):
                continue
            else:
                existing_value += ' ' + tag_name

            track.setComments2(existing_value)
            nb_of_tracks_tagged += 1

            if self._test_mode is True:
                print(track.location())

        print('Tagged ' + str(nb_of_tracks_tagged) + ' tracks.')
        if self._test_mode is False and nb_of_tracks_tagged > 0:
            collection.save()

    def purgeBackups(self) -> None:
        Collection.purgeBackups(test_mode=self._test_mode)

    def shutdown(self) -> None:
        sys.exit(0)

    def printUsage(self) -> None:
        method = None

        if len(self._commands) > 1:
            switch = {
                'topics': TraktorBuddy.printTopics,
                'tag': TraktorBuddy.printTagUsage,
                'license': TraktorBuddy.printLicense
            }

            method = switch.get(self._commands[1])
            if method is None:
                raise ArgumentError('Error: Unknown topic \'' + self._commands[1] + '\'.')

            method()
            return

        TraktorBuddy.printVersion()
        print('')
        print('usage: tktbud <options> <command> <arguments>')
        print('')
        print('The following commands are supported:')
        print('')
        print('   help <topic>       - Show a help message. topic is optional (use \'help topics\' for a list).')
        print('   version            - Print the current version.')
        print('   tag <arguments>    - Add or remove tags (use \'help tag\' for a list of arguments).')
        print('   purge              - Purge all collection backups apart from the most recent.')
        print('')
        print('The following options are supported:')
        print('')
        print('   --help/-h          - Show a help message.')
        print('   --test/-t          - Run in test mode. Affected tracks are printed out. No changes are saved.')
        print('   --all/-a           - Apply command to all tracks instead of just ones in a playlist/folder.')
        print('')

    @classmethod
    def printVersion(cls) -> None:
        print('🎧 Traktor Buddy v' + __version__ + ' 🎧')

    @classmethod
    def printTopics(cls):
        TraktorBuddy.printVersion()
        print('')
        print('Usage:')
        print('   tktbud help tag     - List arguments accepted by the tag command.')
        print('   tktbud help license - Show the license for the app.')
        print('')

    @classmethod
    def printTagUsage(cls):
        TraktorBuddy.printVersion()
        print('')
        print('Usage:')
        print('   tktbud tag add <name> <path>          - Add a tag named \'name\' to all tracks in \'path\'.')
        print('   tktbud tag delete <name> <path>       - Delete a tag named \'name\' for all tracks in \'path\'.')
        print('   tktbud tag rename <old> <new> <path>  - Rename tags named \'old\' to \'new\' for tracks in \'path\'.')
        print('   tktbud tag years <path>               - Add track\'s release year as a tag (i.e. Year:2022).')
        print('')
        print('Playlist/Folder paths are / separated, i.e. \'/Folder1/Folder2/Playlist\'. Use \'\\ \' for spaces.')
        print('If --all option is used the path is ignored and command is applied to all tracks in the collection.')
        print('')

    @classmethod
    def printLicense(cls):
        TraktorBuddy.printVersion()
        print('')
        print('MIT License')
        print('')
        print('Copyright (c) 2022-present Didier Malenfant <coding@malenfant.net>')
        print('')
        print('Permission is hereby granted, free of charge, to any person obtaining a copy')
        print('of this software and associated documentation files (the "Software"), to deal')
        print('in the Software without restriction, including without limitation the rights')
        print('to use, copy, modify, merge, publish, distribute, sublicense, and/or sell')
        print('copies of the Software, and to permit persons to whom the Software is')
        print('furnished to do so, subject to the following conditions:')
        print('')
        print('The above copyright notice and this permission notice shall be included in all')
        print('copies or substantial portions of the Software.')
        print('')
        print('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR')
        print('IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,')
        print('FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE')
        print('AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER')
        print('LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,')
        print('OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE')
        print('SOFTWARE.')
        print('')
        print('Official repo can be found at https://github.com/DidierMalenfant/TraktorBuddy')
        print('')

    @classmethod
    def findAllTracksInFolder(cls, folder: Folder) -> List[Track]:
        result: List[Track] = []

        for folder in folder.folders():
            result = result + TraktorBuddy.findAllTracksInFolder(folder)

        for playlist in folder.playlists():
            result = result + playlist.tracks()

        return result

    @classmethod
    def findAllTracksAtPath(cls, collection: Collection, path: str) -> List[Track]:
        crate = collection.rootFolder().find(path.split('/'))
        if crate is None:
            raise RuntimeError('Could not find any folder or playlist at \'' + path + '\'.')
        elif type(crate) is Folder:
            return TraktorBuddy.findAllTracksInFolder(crate)
        else:
            return crate.tracks()
