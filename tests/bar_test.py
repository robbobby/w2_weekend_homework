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

    def test_bar_has_dukebox(self):
        self.assertEqual("Cafo by Animals as Leaders playing...", self.dukebox.songs[0].play())

    def test_bar_has_staff_member(self):
        self.assertEqual("Barbera", self.bar.staff_list[1].name)

    def test_bar_has_staff__member(self):
        self.assertEqual("Bob", self.bar.staff_list[0].name)

    def test_bhar_has_drinks(self):
        self.assertEqual(FoodAbility.INDIAN, self.bar.food_list[1].ABILITY_REQUIRED)

    def test_bar_has_drink(self):
        self.assertEqual("Cola", self.bar.drinks_list[0].name)

    def test_bar_has__drink(self):
        self.assertEqual("Wine", self.bar.drinks_list[1].name)

    def test_is_in__drinks_list(self):
        self.assertEqual(self.cola, self.bar.is_in_drinks_list(self.cola))

    def test_is_in_drinks_list(self):
        self.assertEqual(False, self.bar.is_in_drinks_list(self.vodka))

    def test_add_to_drinks(self):
        self.bar.add_to_drinks_list(self.vodka)
        self.assertEqual(1, self.bar.drinks_list[-1].stock)

    def test_add_to__drinks(self):
        self.bar.add_to_drinks_list(self.cola)
        self.assertEqual(61, self.bar.drinks_list[0].stock)

    def test_remove_drink_from_list(self):
        self.bar.remove_from_drinks_list("Cola")
        self.assertEqual(1, len(self.bar.drinks_list))