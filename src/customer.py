class Customer:
    def __init__(self, name, age, fun_level, thirst, hunger, wants_alcohol, atmosphere, happy, partner, wallet):
        self.name = name
        self.age = age
        self.thirst = thirst
        self.hunger = hunger
        self.wants_alcohol = wants_alcohol
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

    def remove_room(self):
        self.room = None
        self.__remove_partners_room()

    def remove_partner(self):
        self.partner = None

    def __set_partners_room(self, room):
        self.partner.room = room

    def set_room(self, room):
        self.room = room
        self.__set_partners_room(room)

    def __remove_partners_room(self):
        self.partner.room = None

    def has_money(self, amount):
        if self.wallet >= amount:
            return True
        else:
            return False

    def add_money(self, amount):
        self.wallet += amount

    def take_money(self, amount):
        if self.has_money(amount):
            self.wallet -= amount
            return True
        else:
            return False

    def borrow_money(self, amount):
        if self.partner != None and self.partner.has_money(amount):
            self.add_money(amount)
            self.partner.take_money(amount)
            return True
        else:
            return False

    def set_rooms_guest(self):
        self.room.add_guest(self)
        if self.partner != None:
            self.room.add_guest(self.partner)