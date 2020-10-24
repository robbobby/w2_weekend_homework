import unittest
from src.Bar.food import *
from src.food_ability import *


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Soup", 399, 2, None)
        self.food = Food("Soup", 399, 2, None)

    def test_food_has_name(self):
        self.assertEqual("Soup", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(399, self.food.price)

    def test_food_has_skill_required(self):
        self.assertEqual(2, self.food.SKILL_REQUIRED)

    def test_food_huas_ability_required(self):
        self.assertEqual(None, self.food.ABILITY_REQUIRED)
