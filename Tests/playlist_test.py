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

from TraktorBuddy.playlist import Playlist       # noqa: E402
from TraktorBuddy.track import Track             # noqa: E402
from Tests.mock_tracklist import MockTrackList   # noqa: E402


# -- Tests
@pytest.fixture
def test_playlist() -> Playlist:
    return Playlist(MockTrackList(), ET.fromstring('<NODE TYPE="PLAYLIST" NAME="Beach House Guestmix"><PLAYLIST ENTRIES="12" TYPE="LIST" UUID="83ac15cf29e1429ca9ac8e077f277ed5"><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:La Mezcla (Charles Websters Club Mix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Mo-Cream - On You.m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Retromigration, DimSum - Swiss Paradise.m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Moon Boots, Steven Klavier, Kenny Dope - Tied Up (Kenny Dope Extended Mix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Reelsoul - I Can-t Go For That (Original Mix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Forever (Ramon Tapia Remix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Soulmagic, Saison - Soulmagic (Saison Extended Remix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:01 A House Thing (Original Mix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Someone To Ease My Mind (Original Mix).mp3"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Ready For Your Love (Extended Mix) - Gorgon City and MNEK.m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Scott Diaz, LOA- - Let The Music (Original Mix).m4a"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Sam Miguel, Jay Vegas - Woman (Jay Vegas Remix).m4a"></PRIMARYKEY></ENTRY></PLAYLIST></NODE>'))


def testPlaylistName(test_playlist):
    assert test_playlist.name() == 'Beach House Guestmix'


def testPlaylistTracks(test_playlist):
    tracks: List[Track] = test_playlist.tracks()
    # -- One playlist entry is invalid in our mock track list.
    assert len(tracks) == 11
    assert tracks[0].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:La Mezcla (Charles Websters Club Mix).m4a'
    assert tracks[1].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Mo-Cream - On You.m4a'
    assert tracks[2].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Retromigration, DimSum - Swiss Paradise.m4a'
    assert tracks[3].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Moon Boots, Steven Klavier, Kenny Dope - Tied Up (Kenny Dope Extended Mix).m4a'
    assert tracks[4].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Reelsoul - I Can-t Go For That (Original Mix).m4a'
    assert tracks[5].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Soulmagic, Saison - Soulmagic (Saison Extended Remix).m4a'
    assert tracks[6].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:01 A House Thing (Original Mix).m4a'
    assert tracks[7].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Someone To Ease My Mind (Original Mix).mp3'
    assert tracks[8].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Ready For Your Love (Extended Mix) - Gorgon City and MNEK.m4a'
    assert tracks[9].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Scott Diaz, LOA- - Let The Music (Original Mix).m4a'
    assert tracks[10].location() == 'Macintosh HD/:Users/:didier/:Music/:Gigs/:Sam Miguel, Jay Vegas - Woman (Jay Vegas Remix).m4a'
