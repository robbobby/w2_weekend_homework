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
        self.longs_for = []
        self.room = None

        self.__set_partner()

    def get_joint_wallet(self):
        return self.wallet + self.partner.wallet

    def __set_partner(self):
        if self.partner != None:
            self.partner.partner = self

    def set_partner(self, new_partner):
        # Check to see if we already have a partner
        # Add old partner to longs_for list
        # If we do remove this customer from that customers partner
        # set new partner to partner, add self to partners partner
        if self.partner != None:
            self.add_to_longs_for(self.partner)
            self.remove_self_from_partner()
        self.partner = new_partner
        self.__set_partner()

    def add_to_longs_for(self, person):
        self.longs_for.append(person)

    def remove_self_from_partner(self):
        self.partner.partner = None

    def remove_partner(self):
        self.partner = None