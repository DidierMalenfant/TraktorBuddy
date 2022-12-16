# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import pytest
import sys
import os
import pytz

import xml.etree.ElementTree as ET

from datetime import datetime

# -- We need to import from our parent folder here.
sys.path.append(os.path.join(sys.path[0], '..'))

from TraktorBuddy.track import Track        # noqa: E402
from TraktorBuddy.rating import Rating      # noqa: E402
from TraktorBuddy.key import OpenNotation   # noqa: E402
from TraktorBuddy.color import Color        # noqa: E402
from TraktorBuddy.utility import Utility    # noqa: E402

# TODO: Test for bad date format?


# -- Tests
@pytest.fixture
def test_track() -> Track:
    return Track(ET.fromstring('<ENTRY MODIFIED_DATE="2022/12/12" MODIFIED_TIME="31632" LOCK="1" LOCK_MODIFICATION_TIME="2013-09-02T22:34:23" AUDIO_ID="AZGf//////////////////////////////////////////////////pmq7p6uVuququnnMrJzIjNy6v////////////////////////4/////////////////////////////////////8//////////////////////////iHVVVVZnVVRFeIdmaHaIl2eIeJmIiKmrmavd7/////////////////////////3/////////////////////////////////////////////////////////////////////////////////////////////////////9TEQAAAAAA==" TITLE="Better Love (Axwell Remix)" ARTIST="Deli"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><ALBUM TRACK="42" TITLE="MyRelease"></ALBUM><MODIFICATION_INFO AUTHOR_TYPE="user"></MODIFICATION_INFO><ITUNES PERSISTENT_ID="34A968B76066CC6A"></ITUNES><INFO BITRATE="1411200" GENRE="House" LABEL="My Label" COMMENT="My Comment" RATING="Ramp Up" REMIXER="Axwell" PRODUCER="My Producer" COVERARTID="113/RL3JSJAUHPKA3CXIW2SSBYCRFWLC" MIX="My Mix" KEY="7A" PLAYCOUNT="7" PLAYTIME="401" PLAYTIME_FLOAT="400.629944" RANKING="51" IMPORT_DATE="2011/11/8" LAST_PLAYED="2022/12/8" RELEASE_DATE="2008/1/1" FLAGS="30" FILESIZE="69172" COLOR="1"></INFO><TEMPO BPM="128.000000" BPM_QUALITY="100.000000"></TEMPO><LOUDNESS PEAK_DB="-0.000000" PERCEIVED_DB="-2.362140" ANALYZED_DB="-2.362140"></LOUDNESS><MUSICAL_KEY VALUE="14"></MUSICAL_KEY><CUE_V2 NAME="AutoGrid" DISPL_ORDER="0" TYPE="4" START="53.000000" LEN="0.000000" REPEATS="-1" HOTCUE="-1"></CUE_V2><CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="3" START="53.000000" LEN="0.000000" REPEATS="-1" HOTCUE="0"></CUE_V2><CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="0" START="30053.000000" LEN="0.000000" REPEATS="-1" HOTCUE="1"></CUE_V2><CUE_V2 NAME="Beat Marker" DISPL_ORDER="0" TYPE="1" START="60053.000000" LEN="0.000000" REPEATS="-1" HOTCUE="2"></CUE_V2><CUE_V2 NAME="Beat Marker" DISPL_ORDER="0" TYPE="2" START="360053.000000" LEN="0.000000" REPEATS="-1" HOTCUE="3"></CUE_V2></ENTRY>'))


def testTitle(test_track):
    assert test_track.title() == 'Better Love (Axwell Remix)'


def testArtist(test_track):
    assert test_track.artist() == 'Deli'


def testPlaylistKey(test_track):
    assert test_track._playlistKey() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Better Love (Axwell Remix).m4a'


def testLocation(test_track):
    assert test_track.location() == '/Volumes/Macintosh HD/Users/didier/Music/Gigs/Better Love (Axwell Remix).m4a'


def testModificationDate(test_track):
    date = test_track.modificationDate()
    assert date == pytz.utc.localize(datetime(2022, 12, 12, 8, 47, 12))


def testBeatGridLocked(test_track):
    assert test_track.beatgridLocked() is True


def testBeatGridLockModifiedDate(test_track):
    date = test_track.beatgridLockModifiedDate()
    assert date == pytz.utc.localize(datetime(2013, 9, 2, 22, 34, 23))


def testBitrate(test_track):
    assert test_track.bitrate() == 1411200


def testGenre(test_track):
    assert test_track.genre() == 'House'


def testComments(test_track):
    assert test_track.comments() == 'My Comment'


def testComments2(test_track):
    assert test_track.comments2() == 'Ramp Up'


def testRemixer(test_track):
    assert test_track.remixer() == 'Axwell'


def testKey(test_track):
    assert test_track.key() == '7A'


def testPlayCount(test_track):
    assert test_track.playCount() == 7


def testLength(test_track):
    assert test_track.length() == 400.629944


def testRating(test_track):
    assert test_track.rating() == Rating.OneStar


def testImportDate(test_track):
    assert test_track.importDate() == datetime(2011, 11, 8)


def testLastPlayedDate(test_track):
    assert test_track.lastPlayedDate() == datetime(2022, 12, 8)


def testReleaseDate(test_track):
    assert test_track.releaseDate() == datetime(2008, 1, 1)


def testFileSize(test_track):
    assert test_track.fileSize() == 69172


def testBpm(test_track):
    assert test_track.bpm() == 128.0


def testTraktorKey(test_track):
    assert test_track.traktorKey() == OpenNotation.Key_12m


def testColor(test_track):
    assert test_track.color() == Color.Red


def testLabel(test_track):
    assert test_track.label() == "My Label"


def testProducer(test_track):
    assert test_track.producer() == "My Producer"


def testMix(test_track):
    assert test_track.mix() == "My Mix"


def testRelease(test_track):
    assert test_track.release() == "MyRelease"


def testTrackNumber(test_track):
    assert test_track.trackNumber() == 42


def testNoSampleInfo(test_track):
    assert test_track.isASample() is False


@pytest.fixture
def empty_test_track() -> Track:
    return Track(ET.fromstring('<ENTRY></ENTRY>'))


def testEmptyTitle(empty_test_track):
    assert empty_test_track.title() is None


def testEmptyArtist(empty_test_track):
    assert empty_test_track.artist() is None


def testEmptyLocation(empty_test_track):
    assert empty_test_track.location() is None


def testEmptyBeatGridLocked(empty_test_track):
    assert empty_test_track.beatgridLocked() is False


def testEmptyBeatGridLockModifiedDate(empty_test_track):
    assert empty_test_track.beatgridLockModifiedDate() is None


def testEmptyModificationDate(empty_test_track):
    assert empty_test_track.modificationDate() is None


def testEmptyBitrate(empty_test_track):
    assert empty_test_track.bitrate() is None


def testEmptyGenre(empty_test_track):
    assert empty_test_track.genre() is None


def testEmptyComments(empty_test_track):
    assert empty_test_track.comments() is None


def testEmptyComments2(empty_test_track):
    assert empty_test_track.comments2() is None


def testEmptyRemixer(empty_test_track):
    assert empty_test_track.remixer() is None


def testEmptyKey(empty_test_track):
    assert empty_test_track.key() is None


def testEmptyPlayCount(empty_test_track):
    assert empty_test_track.playCount() is None


def testEmptyLength(empty_test_track):
    assert empty_test_track.length() is None


def testEmptyRating(empty_test_track):
    assert empty_test_track.rating() is None


def testEmptyImportDate(empty_test_track):
    assert empty_test_track.importDate() is None


def testEmptyLastPlayedDate(empty_test_track):
    assert empty_test_track.lastPlayedDate() is None


def testEmptyReleaseDate(empty_test_track):
    assert empty_test_track.releaseDate() is None


def testEmptyFileSize(empty_test_track):
    assert empty_test_track.fileSize() is None


def testEmptyBpm(empty_test_track):
    assert empty_test_track.bpm() is None


def testEmptyTraktorKey(empty_test_track):
    assert empty_test_track.traktorKey() is None


def testEmptyColor(empty_test_track):
    assert empty_test_track.color() is None


def testEmptyLabel(empty_test_track):
    assert empty_test_track.label() is None


def testEmptyProducer(empty_test_track):
    assert empty_test_track.producer() is None


def testEmptyMix(empty_test_track):
    assert empty_test_track.mix() is None


def testEmptyRelease(empty_test_track):
    assert empty_test_track.release() is None


def testEmptyTrackNumber(empty_test_track):
    assert empty_test_track.trackNumber() is None


def testEmptySampleInfo(empty_test_track):
    assert empty_test_track.isASample() is False


def testBeatGridLockIfFalse():
    track = Track(ET.fromstring('<ENTRY MODIFIED_DATE="2022/12/12" MODIFIED_TIME="31632" LOCK="0" LOCK_MODIFICATION_TIME="2013-09-02T22:34:23"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION></ENTRY>'))

    assert track.beatgridLocked() is False


def testTrackIsASample():
    track = Track(ET.fromstring('<ENTRY MODIFIED_DATE="2022/12/12" MODIFIED_TIME="31632" LOCK="1" LOCK_MODIFICATION_TIME="2013-09-02T22:34:23"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><LOOPINFO SAMPLE_TYPE_INFO="1"></LOOPINFO><MUSICAL_KEY VALUE="14"></MUSICAL_KEY></ENTRY>'))

    assert track.isASample() is True


def testOutOfBoundsTraktorKey():
    track = Track(ET.fromstring('<ENTRY MODIFIED_DATE="2022/12/12" MODIFIED_TIME="31632" LOCK="1" LOCK_MODIFICATION_TIME="2013-09-02T22:34:23"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><MUSICAL_KEY VALUE="26"></MUSICAL_KEY></ENTRY>'))

    assert track.traktorKey() is None


def testOutOfBoundsColor():
    track = Track(ET.fromstring('<ENTRY MODIFIED_DATE="2022/12/12" MODIFIED_TIME="31632" LOCK="1" LOCK_MODIFICATION_TIME="2013-09-02T22:34:23"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO COLOR="23"></INFO></ENTRY>'))

    assert track.traktorKey() is None


def testOutOfBoundsRating():
    track = Track(ET.fromstring('<ENTRY MODIFIED_DATE="2022/12/12" MODIFIED_TIME="31632" LOCK="1" LOCK_MODIFICATION_TIME="2013-09-02T22:34:23"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO RANKING="351"></INFO></ENTRY>'))

    assert track.rating() is None


@pytest.fixture
def set_test_track() -> Track:
    Utility._mock_now_date = pytz.utc.localize(datetime(1971, 7, 23, 1, 1, 1))
    return Track(ET.fromstring('<ENTRY><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION></ENTRY>'))


def testSetTitle(set_test_track):
    set_test_track.setTitle('Yeah!')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY TITLE="Yeah!" MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION></ENTRY>'


def testSetArtist(set_test_track):
    set_test_track.setArtist('Alicia Keys')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY ARTIST="Alicia Keys" MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION></ENTRY>'


def testSetBeatGridLocked(set_test_track):
    set_test_track.setBeatGridLocked(False)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY LOCK="0" MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661" LOCK_MODIFICATION_TIME="1971-07-23T01:01:01"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION></ENTRY>'


def testSetBitRate(set_test_track):
    set_test_track.setBitrate(23)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO BITRATE="23"></INFO></ENTRY>'


def testSetGenre(set_test_track):
    set_test_track.setGenre('House Music')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO GENRE="House Music"></INFO></ENTRY>'


def testSetLabel(set_test_track):
    set_test_track.setLabel('Defected Records')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO LABEL="Defected Records"></INFO></ENTRY>'


def testSetProducer(set_test_track):
    set_test_track.setProducer('Steve Angello')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO PRODUCER="Steve Angello"></INFO></ENTRY>'


def testSetMix(set_test_track):
    set_test_track.setMix('Extended Mix')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO MIX="Extended Mix"></INFO></ENTRY>'


def testSetRelease(set_test_track):
    set_test_track.setRelease('Greatest Hits')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><ALBUM TITLE="Greatest Hits"></ALBUM></ENTRY>'


def testSetTrackNumber(set_test_track):
    set_test_track.setTrackNumber('42')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><ALBUM TRACK="42"></ALBUM></ENTRY>'


def testSetComments(set_test_track):
    set_test_track.setComments('Why are we doing this?')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO COMMENT="Why are we doing this?"></INFO></ENTRY>'


def testSetComments2(set_test_track):
    set_test_track.setComments2('Because it must be built.')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO RATING="Because it must be built."></INFO></ENTRY>'


def testSetRemixer(set_test_track):
    set_test_track.setRemixer('Frankie Knuckles')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO REMIXER="Frankie Knuckles"></INFO></ENTRY>'


def testSetKey(set_test_track):
    set_test_track.setKey('12A')
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO KEY="12A"></INFO></ENTRY>'


def testSetPlayCount(set_test_track):
    set_test_track.setPlayCount(4)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO PLAYCOUNT="4"></INFO></ENTRY>'


def testSetLength(set_test_track):
    set_test_track.setLength(453.732)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO PLAYTIME="454" PLAYTIME_FLOAT="453.732000"></INFO></ENTRY>'


def testSetRating(set_test_track):
    set_test_track.setRating(Rating.ThreeStars)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO RANKING="153"></INFO></ENTRY>'


def testSetImportDate(set_test_track):
    set_test_track.setImportDate(datetime(2000, 4, 12))
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO IMPORT_DATE="2000/04/12"></INFO></ENTRY>'


def testSetLastPlayedDate(set_test_track):
    set_test_track.setLastPlayedDate(datetime(1981, 6, 1))
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO LAST_PLAYED="1981/06/01"></INFO></ENTRY>'


def testSetReleaseDate(set_test_track):
    set_test_track.setReleaseDate(datetime(2022, 12, 24))
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO RELEASE_DATE="2022/12/24"></INFO></ENTRY>'


def testSetFileSize(set_test_track):
    set_test_track.setFileSize(4592523)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO FILESIZE="4592523"></INFO></ENTRY>'


def testSetBpm(set_test_track):
    set_test_track.setBpm(123.23)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><TEMPO BPM="123.230000" BPM_QUALITY="100.000000"></TEMPO></ENTRY>'


def testSetTraktorKey(set_test_track):
    set_test_track.setTraktorKey(OpenNotation.Key_2d)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><MUSICAL_KEY VALUE="7"></MUSICAL_KEY></ENTRY>'


def testSetColor(set_test_track):
    set_test_track.setColor(Color.Green)
    string: str = Utility.xmlElementToString(set_test_track._entryElement())
    assert string == '<ENTRY MODIFIED_DATE="1971/07/23" MODIFIED_TIME="3661"><LOCATION DIR="/:Users/:didier/:Music/:Gigs/:" FILE="Better Love (Axwell Remix).m4a" VOLUME="Macintosh HD" VOLUMEID="Macintosh HD"></LOCATION><INFO COLOR="4"></INFO></ENTRY>'
