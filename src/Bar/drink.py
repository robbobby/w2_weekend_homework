class Drink:
    def __init__(self, name, price, units):
        self.units = units
        self.price = price
        self.name = name
        self.stock = 0

    def is_alcoholic(self):
        if self.units == 0:
            return False
        else:
            return True

    def has_stock(self, quantity=1):
        if self.stock - quantity >= 0:
            return True
        return False

    def add_stock(self, quantity=1):
        self.stock += quantity

    def remove_stock(self, quantity=1):
            self.stock -= quantity

    def serve(self, quantity=1):
        if self.has_stock(quantity):
            self.remove_stock(quantity)
            return True
        else:
            return False