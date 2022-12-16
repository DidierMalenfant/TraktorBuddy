# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT


# -- Classes
class MockTrack:
    """Mock collection object to test the playlist class."""

    def __init__(self, location):
        self._location = location

    def location(self):
        return self._location


class MockTrackList:
    """Mock track list object to test the playlist class."""

    def __init__(self):
        self._mock_tracks_map = {
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:La Mezcla (Charles Websters Club Mix).m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Mo-Cream - On You.m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Retromigration, DimSum - Swiss Paradise.m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Moon Boots, Steven Klavier, Kenny Dope - Tied Up (Kenny Dope Extended Mix).m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Reelsoul - I Can-t Go For That (Original Mix).m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Soulmagic, Saison - Soulmagic (Saison Extended Remix).m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:01 A House Thing (Original Mix).m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Someone To Ease My Mind (Original Mix).mp3': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Ready For Your Love (Extended Mix) - Gorgon City and MNEK.m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Scott Diaz, LOA- - Let The Music (Original Mix).m4a': True,
            'Macintosh HD/:Users/:didier/:Music/:Gigs/:Sam Miguel, Jay Vegas - Woman (Jay Vegas Remix).m4a': True
        }

    def trackWithPlaylistKey(self, key: str):
        if self._mock_tracks_map.get(key) is not None:
            return MockTrack(key)

        return None
