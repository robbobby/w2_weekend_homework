from src.genre import Genre

class Song:
    def __init__(self, name, band, year, genre):
        self.name = name
        self.genre = genre
        self.year = year
        self.band = band


    def play(self):
        return f"{self.name} by {self.band} playing..."

    def pause(self):
        return f"{self.name} by {self.band} paused"

    def get_name(self):
        return name
