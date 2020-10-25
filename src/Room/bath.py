from src.Room.bathroom_utility import BathroomUtility


class Bath(BathroomUtility):
    def take_bath(self):
        if self.hygiene - 15 < 0:
            self.hygiene = 0
        else:
            self.hygiene -= 15
        self.set_atmosphere()

    def take_shower(self):
        if self.hygiene - 8 < 0:
            self.hygiene = 0
        else:
            self.hygiene -= 8
        self.set_atmosphere()
