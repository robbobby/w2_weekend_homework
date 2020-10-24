class Song:
    def __init__(self, name, band, year, genre):
        self.name = name
        self.genre = genre
        self.year = year
        self.band = band

    def play_song(self):
        return f"{self.name} by {self.band} playing..."

    def pause_song(self):
        return f"{self.name} by {self.band} paused"
