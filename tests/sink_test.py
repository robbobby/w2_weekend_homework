import unittest
from src.Room.sink import *


class TestSink(unittest.TestCase):
    def setUp(self):
        self.sink = Sink("sink Extra", 7, 100, 10)

    def test_sink_has_model(self):
        self.assertEqual("sink Extra", self.sink.model)

    def test_sink_has_comfort(self):
        self.assertEqual(7, self.sink.comfort)

    def test_sink_has_hygiene(self):
        self.assertEqual(100, self.sink.hygiene)

    def test_sink_has_atmosphere(self):
        self.assertEqual(10, self.sink.atmosphere_level)

    def test_use_sink(self):
        self.sink.wash_hands()
        self.assertEqual(97, self.sink.hygiene)

    def test_use__sink(self):
        for i in range(3):
            self.sink.wash_hands()
        self.assertEqual(91, self.sink.hygiene)

    def test_use____sink(self):
        for i in range(20):
            self.sink.wash_hands()
        self.assertEqual(40, self.sink.hygiene)

    def test_use_shower(self):
        for i in range(11):
            self.sink.brush_teeth()
        self.assertEqual(45, self.sink.hygiene)

    def test_use__shower(self):
        for i in range(8):
            self.sink.brush_teeth()
        self.assertEqual(60, self.sink.hygiene)

    def test_clean_sink(self):
        for i in range(8):
            self.sink.brush_teeth()
        self.sink.clean()
        self.assertEqual(100, self.sink.hygiene)

    def test_set_atmosphere(self):
        self.sink.set_atmosphere()
        self.assertEqual(10, self.sink.atmosphere_level)
    
    def test_set__atmosphere(self):
        for i in range(3):
            self.sink.wash_hands()
        self.assertEqual(9, self.sink.atmosphere_level)

    def test_set___atmosphere(self):
        for i in range(8):
            self.sink.brush_teeth()
        self.assertEqual(6, self.sink.atmosphere_level)