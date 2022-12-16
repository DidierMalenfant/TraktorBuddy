# Traktor Buddy

[![MIT License](https://img.shields.io/github/license/DidierMalenfant/TraktorBuddy)](https://spdx.org/licenses/MIT.html) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/TraktorBuddy.svg)](https://python.org) [![PyPI - Version](https://img.shields.io/pypi/v/TraktorBuddy.svg)](https://pypi.org/project/TraktorBuddy) [![Python package](https://github.com/DidierMalenfant/TraktorBuddy/actions/workflows/python-package.yml/badge.svg)](https://github.com/DidierMalenfant/TraktorBuddy/actions/workflows/python-package.yml)

A helping hand for managing **Traktor** collections.

### Installation

**Traktor Buddy** is a pure Python project. It requires at least [Python](https://python.org) 3.7.

You can install **Traktor Buddy** by typing the following in a terminal window:

```console
pip install TraktorBuddy
```

### Usage from the command line

**Traktor Buddy** supports various commands, sometimes with one or more extra arguments:

```console
tktbud <options> <command> <arguments>
```

The following commands are supported:

```console
help <topic>       - Show a help message. topic is optional (use 'help topics' for a list).
version            - Print the current version.
tag <arguments>    - Add or remove tags (use 'help tag' for a list of arguments).
purge              - Purge all collection backups apart from the most recent.
```

The following options are supported:

```console
--help/-h          - Show a help message.
--test/-t          - Run in test mode. Affected tracks are printed out. No changes are saved.
--all/-a           - Apply command to all tracks instead of just ones in a playlist/folder.
```

**Traktor Buddy** creates a backup of your colllection in `~/.tktbud/backups` before modyfing anything.

### Usage as a library

You can use **Traktor Buddy** in your own **Python** scripts to read and modify **Traktor** collections.

```
import TraktorBuddy

collection = Collection()

for track in collection.tracks():
    print(track.title())
```

The module exposes classes for **Collection**, **Folder**, **Playlist**, **Track**, etc...

### License

**Traktor Buddy** is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
