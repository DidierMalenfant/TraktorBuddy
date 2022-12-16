# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import pytest
import sys
import os

import xml.etree.ElementTree as ET

from typing import List

# -- We need to import from our parent folder here.
sys.path.append(os.path.join(sys.path[0], '..'))

from TraktorBuddy.collection import Collection   # noqa: E402
from TraktorBuddy.folder import Folder           # noqa: E402
from TraktorBuddy.track import Track             # noqa: E402


# -- Tests
@pytest.fixture
def test_collection() -> Collection:
    return Collection(_mock_element=ET.fromstring('<NML VERSION="19"><HEAD COMPANY="www.native-instruments.com" PROGRAM="Traktor"></HEAD><MUSICFOLDERS></MUSICFOLDERS><COLLECTION ENTRIES="3"><ENTRY MODIFIED_DATE="2021/8/30" MODIFIED_TIME="35300" LOCK="1" LOCK_MODIFICATION_TIME="2013-08-27T21:20:33" AUDIO_ID="AaUTMzMzMzMzMzM0MzMzM0NERERa/////////////////////qeO/////////////////////////brryc3Km6ubu6mpqaq6mqqbupeHd3eHd3iJiIiImJmZmpmZr//////////////////+2+/9//////////////////////////3LzM3u3LzM3u3LzMzu3Lzcz+///////////////+zKqZmZiYmImJmZqqu7vO///////////////////+ze7u////////////////////////vv//////////////////////////////////////////////xoUAAAAAAAAA==" TITLE="Tweet It Forever (DBN Bootleg)" ARTIST="Tim Berg, Norman Doray, Sebastien Drums"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Tweet It Forever (DBN Bootleg).mp3" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><MODIFICATION_INFO AUTHOR_TYPE="user"></MODIFICATION_INFO><ITUNES PERSISTENT_ID="CF9BD417201CCC7B"></ITUNES><INFO BITRATE="320000" GENRE="Progressive House" RATING="Peak" REMIXER="DBN" COVERARTID="015/PEU2MKBS4XZKXCBIM2SWAEWHN1FB" KEY="3A" PLAYCOUNT="3" PLAYTIME="421" PLAYTIME_FLOAT="420.545319" RANKING="51" IMPORT_DATE="2013/3/4" LAST_PLAYED="2019/11/15" RELEASE_DATE="2011/5/16" FLAGS="30" FILESIZE="16600"></INFO><TEMPO BPM="127.000000" BPM_QUALITY="100.000000"></TEMPO><LOUDNESS PEAK_DB="-1.132940" PERCEIVED_DB="-0.906166" ANALYZED_DB="-0.906166"></LOUDNESS><MUSICAL_KEY VALUE="22"></MUSICAL_KEY><CUE_V2 NAME="AutoGrid Traktor DJ" DISPL_ORDER="0" TYPE="4" START="472.834000" LEN="0.000000" REPEATS="-1" HOTCUE="-1"></CUE_V2></ENTRY><ENTRY MODIFIED_DATE="2021/8/30" MODIFIED_TIME="35300" LOCK="1" LOCK_MODIFICATION_TIME="2013-08-27T21:20:33" TITLE="Tweet It Forever (DBN Bootleg)" ARTIST="Tim Berg, Norman Doray, Sebastien Drums"></ENTRY><ENTRY MODIFIED_DATE="2022/1/28" MODIFIED_TIME="43188" LOCK="1" LOCK_MODIFICATION_TIME="2013-08-27T21:25:36" AUDIO_ID="AaIAABEjbd3d3d3d3d3d3d3d3d3bvLvMzN3d3d3d3d3d3d3d3d3czMzMzKqYiIiJmHd3d5qYiIiJmHd4ma/+7/7u/+7/7M//7//u/////u//7v/u///v/r3/7v/v7/7v/Kv/7v/u7/7v/svdy67LvdzK61bf/+//7//u/+7f/u//7//+//zP/u/+7v/u7/7v/u7/7u/u7/2qiIiIiId3d3d4q6u7u5mqqqqb3u7u7cmqqqqZ3+7v/u7+7v/bz/7v/+7/7v/sz//v//7/7v7Mz/7v/+7/7v/8zd3d3d3d3d3d3d3d3d3bu7u7mLuqqqqqqqqqqqqqqqqqqqqqq4QhEA==" TITLE="Sunrise (Original Mix)" ARTIST="A &amp; P Project"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Sunrise (Original Mix).mp3" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><MODIFICATION_INFO AUTHOR_TYPE="user"></MODIFICATION_INFO><ITUNES PERSISTENT_ID="0902955ED0B195A1"></ITUNES><INFO BITRATE="222327" GENRE="House" RATING="End" COVERARTID="050/SJNTY0ATGFG10CYJRATMAD0DDOFB" KEY="12A" PLAYCOUNT="7" PLAYTIME="418" PLAYTIME_FLOAT="417.515106" RANKING="51" IMPORT_DATE="2011/6/4" LAST_PLAYED="2021/5/7" RELEASE_DATE="2003/1/1" FLAGS="30" FILESIZE="11616"></INFO><TEMPO BPM="127.782997" BPM_QUALITY="100.000000"></TEMPO><LOUDNESS PEAK_DB="-0.014703" PERCEIVED_DB="1.342300" ANALYZED_DB="1.342300"></LOUDNESS><MUSICAL_KEY VALUE="13"></MUSICAL_KEY><CUE_V2 NAME="AutoGrid" DISPL_ORDER="0" TYPE="4" START="1479.000000" LEN="0.000000" REPEATS="-1" HOTCUE="-1"></CUE_V2><CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="3" START="7107.000000" LEN="0.000000" REPEATS="-1" HOTCUE="0"></CUE_V2><CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="1" START="67207.000000" LEN="0.000000" REPEATS="-1" HOTCUE="1"></CUE_V2><CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="2" START="352678.000000" LEN="0.000000" REPEATS="-1" HOTCUE="2"></CUE_V2></ENTRY></COLLECTION><PLAYLISTS><NODE TYPE="FOLDER" NAME="$ROOT"><SUBNODES COUNT="1"><NODE TYPE="FOLDER" NAME="Damien Plays Records"><SUBNODES COUNT="1"><NODE TYPE="FOLDER" NAME="Episodes"><SUBNODES COUNT="1"><NODE TYPE="PLAYLIST" NAME="Beach House Guestmix"><PLAYLIST ENTRIES="2" TYPE="LIST" UUID="83ac15cf29e1429ca9ac8e077f277ed5"><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Tweet It Forever (DBN Bootleg).mp3"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Sunrise (Original Mix).mp3"></PRIMARYKEY></ENTRY></PLAYLIST></NODE></SUBNODES></NODE></SUBNODES></NODE></SUBNODES></NODE></PLAYLISTS></NML>'))


def testCollectionEntryWithNoLocation(test_collection):
    tracks: List[Track] = test_collection.tracks()
    assert len(tracks) == 2


# TODO: Those should be moved into track lists tests
def testCollectionTrackWithPlaylistKey(test_collection):
    track: Track = test_collection.trackWithPlaylistKey('Macintosh HD/:Users/:didier/:Music/:Gigs/:Sunrise (Original Mix).mp3')
    assert track is not None
    assert track.title() == 'Sunrise (Original Mix)'


def testCollectionUnknownTrackWithPlaylistKey(test_collection):
    track: Track = test_collection.trackWithPlaylistKey('Macintosh HD/:Users/:didier/:Music/:Gigs/:This does not exist.m4a')
    assert track is None


def testRootFolder(test_collection):
    root_folder: Folder = test_collection.rootFolder()
    assert root_folder is not None
    assert root_folder.name() == '$ROOT'
