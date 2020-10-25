from src.genre import Genre
from src.song import Song


class DukeBox:
    def __init__(self, songs, price, playlist):
        self.songs = songs
        self.price = price
        self.playlist = playlist
        # self.current_song = Song("Not playing", "No Band", 1, Genre.NONE)
        self.current_song = Song
        self.is_playing = False

    def add_song_to_songs(self, new_song):
        self.songs.append(new_song)

    def get_song(self, position):
        print(self.songs[position])

    def get_song_with_name(self, name):
        for song in self.songs:
            if song.name.title() == name.title():
                return song

        return None

    def get_song_by_band(self, band):
        songs_by_band = [song for song in self.songs if song.band.title() == band.title()]
        # for song in self.songs:
        #     if song.band.title() == band.title():
        #         songs_by_band.append(song)

        return songs_by_band

    def build_string_did_you_mean(self, song_list):
        possible_songs = "Did you mean "
        for song in song_list:
            possible_songs += song.name
            if song != song_list[-1]:
                possible_songs += " or "
        possible_songs += " by " + song_list[0].band

        return possible_songs

    def get_song_by_band_and_name(self, name, band):
        song_list = self.get_song_by_band(band)
        for song in song_list:
            if song.name == name:
                return song

        return self.build_string_did_you_mean(song_list)

    def get_all_songs_with_genre(self, genre):
        song_list = []
        for song in self.songs:
            if song.genre == genre:
                song_list.append(song)

        return song_list

    def set_current_song(self, song_name):
        self.current_song = self.get_song_with_name(song_name)
        self.is_playing = True

    def song_finished(self):
        self.is_playing = False
        self.current_song = None