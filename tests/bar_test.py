import unittest
from src.Bar.bar import *


class TestBar(unittest.TestCase):
    def setUp(self):
                                    ##### Staff #####
        self.staff_member = Staff("Bob", 1, 21, 4, Job.CHEF, [FoodAbility.CHINESE])
        self.staff_member2 = Staff("Barbera", 10, 92, 4, Job.DOORMAN, [FoodAbility.INDIAN])
        self.staff_member3 = Staff("George", 100, 12, 4, Job.CHEF, [FoodAbility.NONE])

                                    ##### Drinks #####
        self.drink = Drink("Wine", 899, 67)

                                    ##### Food #####
        self.food = Food("Soup", 399, 2, None)
        self.food_1 = Food("Curry", 399, 2, FoodAbility.INDIAN)
