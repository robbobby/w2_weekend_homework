import unittest
from src.Bar.drink import *


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Wine", 899, 67)

    def test_drink_has_name(self):
        self.assertEqual("Wine", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(899, self.drink.price)

    def test_drink_has_units(self):
        self.assertEqual(67, self.drink.units)