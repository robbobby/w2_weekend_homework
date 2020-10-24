import unittest
from src.Bar.drink import *


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.wine = Drink("Wine", 899, 67)
        self.cola = Drink("Cola", 199, 0)

    def test_drink_has_name(self):
        self.assertEqual("Wine", self.wine.name)

    def test_drink_has_price(self):
        self.assertEqual(899, self.wine.price)

    def test_drink_has_units(self):
        self.assertEqual(67, self.wine.units)

    def test_is_alcoholic(self):
        self.assertEqual(False, self.cola.is_alcoholic())

    def test_is__alcoholic(self):
        self.assertEqual(True, self.wine.is_alcoholic())
