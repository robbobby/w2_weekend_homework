import unittest
from src.song import Song
from src.genre import Genre


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL)

    def test_song_has_name(self):
        self.assertEqual("Cafo", self.song.name)

    def test_song_has_band(self):
        self.assertEqual("Animals as Leaders", self.song.band)

    def test_song_has_year(self):
        self.assertEqual(2009, self.song.year)

    def test_song_has_genre(self):
        self.assertEqual(Genre.ALTERNATIVE_METAL, self.song.genre)

    def test_song_play(self):
        self.assertEqual("Cafo by Animals as Leaders playing...", self.song.play())

    def test_song_paused(self):
        self.assertEqual("Cafo by Animals as Leaders paused", self.song.pause())