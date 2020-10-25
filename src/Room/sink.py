from src.Room.bathroom_utility import BathroomUtility


class Sink(BathroomUtility):
    def wash_hands(self):
        if self.hygiene - 3 < 0:
            self.hygiene = 0
        else:
            self.hygiene -= 3
        self.set_atmosphere()

    def brush_teeth(self):
        if self.hygiene - 5 < 0:
            self.hygiene = 0
        else:
            self.hygiene -= 5
        self.set_atmosphere()
