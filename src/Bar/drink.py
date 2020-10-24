class Drink:
    def __init__(self, name, price, units):
        self.units = units
        self.price = price
        self.name = name

    def is_alcoholic(self):
        if self.units == 0:
            return False
        else:
            return True
