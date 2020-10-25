class Customer:
    def __init__(self, name, age, fun_level, thirst, hunger, wants_alcohol, atmosphere, happy, partner, wallet):
        self.name = name
        self.age = age
        self.thirst = thirst
        self.hunger = hunger
        self.wants_alhohol = wants_alcohol
        self.fun_level = fun_level
        self.atmosphere = atmosphere
        self.happy = happy
        self.partner = partner
        self.wallet = wallet

        self.set_partner()

    def get_joint_wallet(self):
        return self.wallet + self.partner.wallet

    def set_partner(self):
        if self.partner != None:
            self.partner.partner = self
