from src.Room.bathroom_utility import BathroomUtility


class Toilet(BathroomUtility):
    def take_number1(self):
        if self.hygiene - 3 < 0:
            self.hygiene = 0
        else:
            self.hygiene -= 3

    def take_number2(self):
        if self.hygiene - 10 < 0:
            self.hygiene = 0
        else:
            self.hygiene -= 10