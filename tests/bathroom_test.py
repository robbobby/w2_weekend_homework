import unittest

from src.Room.bath import Bath
from src.Room.bathroom import *
from src.Room.sink import Sink
from src.Room.toilet import Toilet


class TestBathroom(unittest.TestCase):
    def setUp(self):
        self.bath = Bath("Bath Extra", 7, 100, 10)
        self.toilet = Toilet("ToLet Amaze", 7, 100, 10)
        self.sink = Sink("sink Extra", 7, 100, 10)

        self.bathroom = Bathroom(self.sink, self.bath, self.toilet, RoomType.TRIPLE)

    def test_bathroom_has_room_quality(self):
        self.assertEqual(RoomType.TRIPLE, self.bathroom.quality)

    def test_bathroom_has_toilet(self):
        self.assertEqual(type(self.sink), type(self.bathroom.sink))

    def test_bathroom_has_toilet(self):
        self.assertEqual(type(self.bath), type(self.bathroom.bath))

    def test_bathroom_has_toilet(self):
        self.assertEqual(type(self.toilet), type(self.bathroom.toilet))

    def test_bathroom_has_atmosphere(self):
        self.assertEqual(17, self.bathroom.atmosphere)