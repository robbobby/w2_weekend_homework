import unittest

from src.Room.bath import Bath
from src.Room.bathroom import Bathroom
from src.Room.room import *
from src.Room.room_types import RoomType
from src.Room.sink import Sink
from src.Room.toilet import Toilet
from src.dukebox import DukeBox
from src.genre import Genre
from src.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.bath = Bath("Bath Extra", 7, 100, 10)
        self.toilet = Toilet("ToLet Amaze", 7, 100, 10)
        self.sink = Sink("sink Extra", 7, 100, 10)

        self.song = [Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL),
                     Song("Electric Sunrise", "Plini", 2016, Genre.PROG_METAL),
                     Song("Pastures", "Plini", 2016, Genre.PROG_METAL)]

        self.dukebox = DukeBox(self.song, 99, [])

        self.room = Room([], self.dukebox, RoomType.DELUXE)

        self.bathroom = Bathroom(self.sink, self.bath, self.toilet, self.room.room_quality)

    def test_room_has_rooms(self):
        self.assertEqual([], self.room.rooms)

    def test_can_add_room(self):
        self.room.add_room(self.bathroom)
        self.assertEqual(self.bathroom, self.room.rooms[0])

    def test_room_has_type(self):
        self.assertEqual(RoomType.DELUXE, self.room.room_quality)

    def test_room_inherit_type(self):
        self.room.add_room(self.bathroom)
        self.assertEqual(RoomType.DELUXE, self.room.rooms[0].room_type)
        self.assertEqual(self.room.room_quality, self.room.rooms[0].room_type)

    def test_room_atmosphere(self):
        self.room.set_atmosphere()
        self.assertEqual(0, self.room.atmosphere)


    def test_room__atmosphere(self):
        self.room.add_room(self.bathroom)
        self.room.set_atmosphere()
        self.assertEqual(22, self.room.atmosphere)
