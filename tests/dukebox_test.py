import unittest
from src.dukebox import *
from src.song import *


class TestDukeBox(unittest.TestCase):
    def setUp(self):
        self.song = [Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL),
                    Song("Electric Sunrise", "Plini", 2016, Genre.PROG_METAL),
                    Song("Pastures", "Plini", 2016, Genre.PROG_METAL)]
        self.dukebox = DukeBox(self.song, 99, [])

    def test_dukebox_has_song(self):
        self.assertEqual("Cafo", self.dukebox.songs[0].name)  ### works fine

    def test_add_song_to_list(self):
        new_song = Song("Bohemian Rhapsody", "Queen", 1975, Genre.POP)
        self.dukebox.add_song_to_songs(new_song)
        self.assertEqual("Bohemian Rhapsody", self.dukebox.songs[-1].name)  ### works fine

    def test_add_song_to__list_and_old_are_ok(self):
        new_song = Song("Bohemian Rhapsody", "Queen", 1975, Genre.POP)
        self.dukebox.add_song_to_songs(new_song)
        self.assertEqual("Pastures", self.dukebox.songs[-2].name)  ### works fine

    def test_find_song_by_name(self):
        self.assertEqual(self.dukebox.songs[0], self.dukebox.get_song_with_name("Cafo"))

    def test_find_song_by__name(self):
        self.assertEqual(None, self.dukebox.get_song_with_name("No name"))

    def test_find_song_by_band(self):
        self.assertEqual(1, len(self.dukebox.get_song_by_band("Animals as leaders")))

    def test_find_song_by_band_and_name(self):
        song_gotten = self.dukebox.get_song_by_band_and_name("Cafo", "Animals as leaders")
        self.assertEqual("Cafo", song_gotten.name)

    def test_find_song_by_band_and_name(self):
        song_gotten = self.dukebox.get_song_by_band_and_name("afo", "Animals as leaders")
        print(self.dukebox.get_song_by_band_and_name("afo", "Animals as leaders"))
        self.assertEqual("Did you mean Cafo", self.dukebox.get_song_by_band_and_name("afo", "Animals as leaders"))

    def test_find_song_by_band_and_name(self):
        song_gotten = self.dukebox.get_song_by_band_and_name("afo", "Animals as leaders")
        print(self.dukebox.get_song_by_band_and_name("afo", "Plini"))
        self.assertEqual("Did you mean Electric Sunrise or Pastures by Plini", self.dukebox.get_song_by_band_and_name("wrong song name", "Plini"))

    def test_get_all_songs_with_genre(self):
        self.assertEqual(2, len(self.dukebox.get_all_songs_with_genre(Genre.PROG_METAL)))

    def test_get_all_songs_with_genre(self):
        self.assertEqual(1, len(self.dukebox.get_all_songs_with_genre(Genre.ALTERNATIVE_METAL)))

    # def test_current_song_empty_init(self):
    #     self.assertIsNone(self.dukebox.current_song, "Current song is not none")

    def test_set_current_song(self):
        self.dukebox.set_current_song("Cafo")
        print(self.dukebox.current_song.name)
        self.assertEqual(self.dukebox.songs[0].name, self.dukebox.current_song.name)