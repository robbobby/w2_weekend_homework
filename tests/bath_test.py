import unittest
from src.Room.bath import *


class TestBath(unittest.TestCase):
    def setUp(self):
        self.bath = Bath("Bath Extra", 7, 100, 10)

    def test_bath_has_model(self):
        self.assertEqual("Bath Extra", self.bath.model)

    def test_bath_has_comfort(self):
        self.assertEqual(7, self.bath.comfort)

    def test_bath_has_hygiene(self):
        self.assertEqual(100, self.bath.hygiene)

    def test_bath_has_atmosphere(self):
        self.assertEqual(10, self.bath.atmosphere_level)

    def test_use_bath(self):
        self.bath.take_bath()
        self.assertEqual(85, self.bath.hygiene)

    def test_use__bath(self):
        for i in range(3):
            self.bath.take_bath()
        self.assertEqual(65, self.bath.hygiene)

    def test_use__bath(self):
        for i in range(20):
            self.bath.take_bath()
        self.assertEqual(0, self.bath.hygiene)

    def test_use___bath(self):
        self.bath.take_shower()
        self.assertEqual(92, self.bath.hygiene)

    def test_use_shower(self):
        for i in range(11):
            self.bath.take_shower()
        self.assertEqual(12, self.bath.hygiene)

    def test_use__shower(self):
        for i in range(8):
            self.bath.take_shower()
        self.assertEqual(36, self.bath.hygiene)

    def test_clean_bath(self):
        for i in range(8):
            self.bath.take_shower()
        self.bath.clean()
        self.assertEqual(100, self.bath.hygiene)

    def test_set_atmosphere(self):
        self.bath.set_atmosphere()
        self.assertEqual(10, self.bath.atmosphere_level)

    def test_set__atmosphere(self):
        for i in range(3):
            self.bath.take_bath()
        self.assertEqual(5, self.bath.atmosphere_level)

    def test_set___atmosphere(self):
        for i in range(8):
            self.bath.take_shower()
        self.assertEqual(3, self.bath.atmosphere_level)