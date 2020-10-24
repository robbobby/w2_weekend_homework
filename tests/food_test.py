import unittest
from src.Bar.food import *
from src.food_ability import *


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Soup", 399, 2, None)
        self.food_1 = Food("Curry", 399, 2, FoodAbility.INDIAN)

    def test_food_has_name(self):
        self.assertEqual("Soup", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(399, self.food.price)

    def test_food_has_skill_required(self):
        self.assertEqual(2, self.food.SKILL_REQUIRED)

    def test_food_has_ability_required(self):
        self.assertEqual(None, self.food.ABILITY_REQUIRED)

    def test_food_has__ability_required(self):
        self.assertEqual(FoodAbility.INDIAN, self.food_1.ABILITY_REQUIRED)

    def test_food_has_stock(self):
        self.assertEqual(0, self.food.stock)

    def test_add_to_stock_default_value(self):
        self.food.add_stock()
        self.assertEqual(1, self.food.stock)

    def test_add_to_stock(self):
        self.food.add_stock(1)
        self.assertEqual(1, self.food.stock)

    def test__add_to_stock(self):
        self.food.add_stock(10)
        self.food.add_stock(10)
        self.assertEqual(20, self.food.stock)

    def test_check_has_stock(self):
        self.assertEqual(False, self.food.has_stock())

    def test__check_has_stock(self):
        self.food.add_stock(2)
        self.assertEqual(True, self.food.has_stock(2))

    def test_reduce_stock(self):
        self.food.add_stock(10)
        self.food.serve(11)
        self.assertEqual(10, self.food.stock)

    def test__reduce_stock(self):
        self.food.add_stock(10)
        self.food.serve(9)
        self.assertEqual(1, self.food.stock)