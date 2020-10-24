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





    def test_drink_has_stock(self):
        self.assertEqual(0, self.wine.stock)

    def test_add_to_stock_default_value(self):
        self.wine.add_stock()
        self.assertEqual(1, self.wine.stock)

    def test_add_to_stock(self):
        self.wine.add_stock(1)
        self.assertEqual(1, self.wine.stock)

    def test__add_to_stock(self):
        self.wine.add_stock(10)
        self.wine.add_stock(10)
        self.assertEqual(20, self.wine.stock)

    def test_check_has_stock(self):
        self.assertEqual(False, self.wine.has_stock())

    def test__check_has_stock(self):
        self.wine.add_stock(2)
        self.assertEqual(True, self.wine.has_stock(2))

    def test_reduce_stock(self):
        self.wine.add_stock(10)
        self.wine.serve(11)
        self.assertEqual(10, self.wine.stock)

    def test__reduce_stock(self):
        self.wine.add_stock(10)
        self.wine.serve(9)
        self.assertEqual(1, self.wine.stock)