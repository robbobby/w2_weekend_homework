class Food:
    def __init__(self, name, price, skill_required, ability_required):
        self.ABILITY_REQUIRED = ability_required
        self.SKILL_REQUIRED = skill_required
        self.price = price
        self.name = name