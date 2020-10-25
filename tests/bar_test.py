import unittest
from src.Bar.bar import *
from src.Bar.drink import Drink
from src.Bar.food import Food
from src.dukebox import DukeBox
from src.food_ability import FoodAbility
from src.genre import Genre
from src.song import Song
from src.staff import Staff
from src.staff_jobs import Job


class TestBar(unittest.TestCase):
    def setUp(self):
                                    ##### Staff #####
        self.staff1 = Staff("Bob", 1, 21, 4, Job.CHEF, [FoodAbility.CHINESE])
        self.staff2 = Staff("Barbera", 10, 92, 4, Job.DOORMAN, [FoodAbility.INDIAN])
        self.staff3 = Staff("George", 100, 12, 4, Job.CHEF, [FoodAbility.NONE])

                                    ##### Drinks #####
        self.wine = Drink("Wine", 899, 67)
        self.cola = Drink("Cola", 199, 0)
        self.vodka = Drink("Vodka", 299, 0)

                                    ##### Food #####
        self.food = Food("Soup", 399, 2, None)
        self.food_1 = Food("Curry", 399, 2, FoodAbility.INDIAN)
        self.food_not = Food("Chinese", 899, 2, FoodAbility.CHINESE)

                                    ##### Songs #####

        self.song = [Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL),
                    Song("Electric Sunrise", "Plini", 2016, Genre.PROG_METAL),
                    Song("Pastures", "Plini", 2016, Genre.PROG_METAL)]

                                    ##### Duke Box #####
        self.dukebox = DukeBox(self.song, 99, [])

                                    ##### Bar #####
        self.bar = Bar(self.dukebox, [self.staff1, self.staff2, self.staff3], [self.cola, self.wine], [self.food, self.food_1])

        self.bar.drinks_list[0].add_stock(60)
        self.bar.drinks_list[1].add_stock(90)
        self.bar.food_list[0].add_stock(100)
        self.bar.food_list[1].add_stock(70)


                                    ##### Object/Properties test #####
    def test_bar_has_dukebox(self):
        self.assertEqual("Cafo by Animals as Leaders playing...", self.dukebox.songs[0].play())

    def test_bar_has_staff_member(self):
        self.assertEqual("Barbera", self.bar.staff_list[1].name)

    def test_bar_has_staff__member(self):
        self.assertEqual("Bob", self.bar.staff_list[0].name)

    def test_bar_has_food(self):
        self.assertEqual(FoodAbility.INDIAN, self.bar.food_list[1].ABILITY_REQUIRED)

                                    ##### Drinks Tests #####

    def test_bar_has__drink(self):
        self.assertEqual("Cola", self.bar.drinks_list[0].name)

    def test_bar_has___drink(self):
        self.assertEqual("Wine", self.bar.drinks_list[1].name)

    def test_is_in__drinks_list(self):
        self.assertEqual(self.cola, self.bar.is_in_menu_list(self.cola, self.bar.drinks_list))

    def test_is_in_drinks_list(self):
        self.assertEqual(False, self.bar.is_in_menu_list(self.vodka, self.bar.drinks_list))

    def test_add_to_drinks(self):
        self.bar.add_to_menu_list(self.vodka, self.bar.drinks_list)
        self.assertEqual(1, self.bar.drinks_list[-1].stock)

    def test_add_to__drinks(self):
        self.bar.add_to_menu_list(self.cola, self.bar.drinks_list)
        self.assertEqual(61, self.bar.drinks_list[0].stock)

    def test_remove_drink_from_list(self):
        self.bar.remove_from_menu_list("Cola", self.bar.drinks_list)
        self.assertEqual(1, len(self.bar.drinks_list))

                                ##### Food List Tests #####
    def test_is_in_food_list(self):
        self.assertEqual(self.food, self.bar.is_in_menu_list(self.food, self.bar.food_list))

    def test_is_in_food__list(self):
        self.assertEqual(False, self.bar.is_in_menu_list(self.food_not, self.bar.food_list))

    def test_add_food_to_list(self):
        self.bar.add_to_menu_list(self.food_not, self.bar.food_list)
        self.assertEqual(1, self.bar.food_list[-1].stock)
        self.assertEqual(self.food_not.name, self.bar.food_list[-1].name)

    def test_add_food_to__list(self):
        self.bar.add_to_menu_list(self.food, self.bar.food_list)
        self.assertEqual(101, self.bar.food_list[0].stock)

    def test_remove_food_from_list(self):
        self.bar.remove_from_menu_list("Curry", self.bar.food_list)
        self.assertEqual(1, len(self.bar.food_list))

                                ##### Staff Tests #####
    def test_remove_new_staff(self):
        self.bar.remove_staff_member(self.staff1.name)
        self.assertEqual(2, len(self.bar.staff_list))

    def test_add_new__staff(self):
        self.bar.add_staff_member(self.staff1)
        self.assertEqual(4, len(self.bar.staff_list))

    def test_get_staff_member_by_name(self):
        self.assertEqual(self.bar.staff_list[0], self.bar.get_staff_member_by_name(self.bar.staff_list[0].name))

    def test_bar_has_till(self):
        self.assertEqual(10000, self.bar.till)

    def test_bar_can_add_to_till(self):
        self.bar.add_to_till(100)
        self.assertEqual(10100, self.bar.till)

    def test_bar_can_take_off_till(self):
        self.bar.take_from_till(1000)
        self.assertEqual(9000, self.bar.till)

    def test_bar_can_take_from__till(self):
        self.bar.take_from_till(100000)
        self.assertEqual(10000, self.bar.till)

