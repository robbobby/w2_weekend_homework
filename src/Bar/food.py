class Food:
    def __init__(self, name, price, skill_required, ability_required):
        self.ABILITY_REQUIRED = ability_required
        self.SKILL_REQUIRED = skill_required
        self.price = price
        self.name = name
        self.stock = 0  # External Use

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