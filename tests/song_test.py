import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Cafo", "Animals as Leaders", 2009, "Altnerative Metal")

    def test_song_has_name(self):
        self.assertEqual("Cafo", self.song.name)

    def test_song_has_band(self):
        self.assertEqual("Animals as Leaders", self.song.band)

    def test_song_has_year(self):
        self.assertEqual(2009, self.song.year)

    def test_song_has_genre(self):
        self.assertEqual("Altnerative Metal", self.song.genre)
