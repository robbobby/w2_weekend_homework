import unittest
from src.Room.toilet import *


class TestToilet(unittest.TestCase):
    def setUp(self):
        self.toilet = Toilet("ToLet Amaze", 7, 100, 10)

    def test_toilet_has_model(self):
        self.assertEqual("ToLet Amaze", self.toilet.model)

    def test_toilet_has_comfort(self):
        self.assertEqual(7, self.toilet.comfort)

    def test_toilet_has_model(self):
        self.assertEqual(100, self.toilet.hygiene)

    def test_toilet_has_model(self):
        self.assertEqual(10, self.toilet.atmosphere_level)

    def test_use_toilet_num1(self):
        self.toilet.take_number1()
        self.assertEqual(97, self.toilet.hygiene)

    def test_use_toilet__num1(self):
        for i in range(40):
            self.toilet.take_number1()
        self.assertEqual(0, self.toilet.hygiene)

    def test_use_toilet___num1(self):
        for i in range(20):
            self.toilet.take_number1()
        self.assertEqual(40, self.toilet.hygiene)

    def test_use_toilet_num2(self):
        self.toilet.take_number2()
        self.assertEqual(90, self.toilet.hygiene)

    def test_use_toilet__num2(self):
        for i in range(11):
            self.toilet.take_number2()
        self.assertEqual(0, self.toilet.hygiene)

    def test_use_toilet___num2(self):
        for i in range(8):
            self.toilet.take_number2()
        self.assertEqual(20, self.toilet.hygiene)

    def test_clean_toilet(self):
        for i in range(8):
            self.toilet.take_number2()
        self.toilet.clean()
        self.assertEqual(100, self.toilet.hygiene)

    def test_set_atmosphere(self):
        self.toilet.set_atmosphere()
        self.assertEqual(10, self.toilet.atmosphere_level)

    def test_set__atmosphere(self):
        for i in range(8):
            self.toilet.take_number1()
        self.toilet.set_atmosphere()
        self.assertEqual(7, self.toilet.atmosphere_level)

    def test_set___atmosphere(self):
        for i in range(8):
            self.toilet.take_number2()
        self.toilet.set_atmosphere()
        self.assertEqual(2, self.toilet.atmosphere_level)