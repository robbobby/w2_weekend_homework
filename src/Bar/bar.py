class Bar:
    def __init__(self, dukebox, staff, drinks, food):
        self.food_list = food
        self.drinks_list = drinks
        self.staff_list = staff
        self.dukebox = dukebox
        self.till = 10000

    def is_in_menu_list(self, new_drink, menu):
        for drink in menu:
            if drink.name == new_drink.name:
                return drink

        return False

    def add_to_menu_list(self, new_item, menu):
        if self.is_in_menu_list(new_item, menu):
            for drink in menu:
                if drink.name == new_item.name:
                    drink.add_stock()
        else:
            menu.append(new_item)
            menu[-1].add_stock()

    def remove_from_menu_list(self, new_item, menu):
        for item in menu:
            if item.name == new_item:
                menu.remove(item)

    def remove_staff_member(self, staff_name):
        for staff in self.staff_list:
            if staff.name == staff_name:
                self.staff_list.remove(staff)

    def add_staff_member(self, staff):
        self.staff_list.append(staff)

    def get_staff_member_by_name(self, staff_name):
        for staff in self.staff_list:
            if staff.name == staff_name:
                return staff

    def add_to_till(self, amount):
        self.till += amount

    def take_from_till(self, amount):
        if self.till - amount > 0:
            self.till -= amount
            return True
        else:
            return False

