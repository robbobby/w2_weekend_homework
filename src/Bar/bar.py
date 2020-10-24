class Bar:
    def __init__(self, dukebox, staff, drinks, food):
        self.food_list = food
        self.drinks_list = drinks
        self.staff_list = staff
        self.dukebox = dukebox

    def is_in_drinks_list(self, new_drink):
        for drink in self.drinks_list:
            if drink.name == new_drink.name:
                return drink

        return False

    def add_to_drinks_list(self, new_drink):
        if self.is_in_drinks_list(new_drink):
            for drink in self.drinks_list:
                if drink.name == new_drink.name:
                    drink.add_stock()
        else:
            self.drinks_list.append(new_drink)
            self.drinks_list[-1].add_stock()

    def remove_from_drinks_list(self, drink_name):
        for drink in self.drinks_list:
            if drink.name == drink_name:
                self.drinks_list.remove(drink)
