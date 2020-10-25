# import unittest
#
# from src.Room.bath import Bath
# from src.Room.bathroom import Bathroom
# from src.Room.room import *
# from src.Room.room_types import RoomType
# from src.Room.sink import Sink
# from src.Room.toilet import Toilet
# from src.customer import Customer
# from src.dukebox import DukeBox
# from src.genre import Genre
# from src.song import Song
#
#
# class TestRoom(unittest.TestCase):
#     def setUp(self):
#
#                                 ##### Customer Set Up #####
#         self.customer = Customer("Jeff", 24, 80, 70, 60, 10, 0, 90, None, 100)
#         self.customer2 = Customer("Margaret", 15, 83, 70, 99, 10, 0, 90, self.customer, 200)
#         self.customer3 = Customer("Dorothy", 47, 83, 70, 99, 10, 0, 90, None, 200)
#         self.customer4 = Customer("Humphrey", 15, 83, 70, 14, 10, 0, 90, None, 200)
#
#                                 ##### Room Set Up #####
#         self.bath = Bath("Bath Extra", 7, 100, 10)
#         self.toilet = Toilet("ToLet Amaze", 7, 100, 10)
#         self.sink = Sink("sink Extra", 7, 100, 10)
#
#         self.song = [Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL),
#                      Song("Electric Sunrise", "Plini", 2016, Genre.PROG_METAL),
#                      Song("Pastures", "Plini", 2016, Genre.PROG_METAL)]
#
#         self.dukebox = DukeBox(self.song, 99, [])
#
#         self.room = Room([], self.dukebox, RoomType.DELUXE)
#
#         self.bathroom = Bathroom(self.sink, self.bath, self.toilet, self.room.quality)
#
#     def test_room_has_rooms(self):
#         self.assertEqual([], self.room.rooms)
#
#     def test_can_add_room(self):
#         self.room.add_room(self.bathroom)
#         self.assertEqual(self.bathroom, self.room.rooms[0])
#
#     def test_room_has_type(self):
#         self.assertEqual(RoomType.DELUXE, self.room.quality)
#
#     def test_room_inherit_type(self):
#         self.room.add_room(self.bathroom)
#         self.assertEqual(RoomType.DELUXE, self.room.rooms[0].quality)
#         self.assertEqual(self.room.quality, self.room.rooms[0].quality)
#
#     def test_room_atmosphere(self):
#         self.room.set_atmosphere()
#         self.assertEqual(0, self.room.atmosphere)
#
#     def test_room__atmosphere(self):
#         self.room.add_room(self.bathroom)
#         self.room.set_atmosphere()
#         self.assertEqual(22, self.room.atmosphere)
#
#     def test_room_has_guest_list(self):
#         self.assertEqual([], self.room.guests)
#
#     def test_room_can_add_guest(self):
#         self.room.add_guest(self.customer)
#         self.assertEqual(self.customer, self.room.guests[0])
#
#     def test_room_can_add_guest(self):
#         self.room.add_guest(self.customer)
#         self.room.add_guest(self.customer)
#         self.assertEqual(1, len(self.room.guests))
#
#     def test_room_can_remove_guest(self):
#         self.room.add_guest(self.customer)
#         self.room.remove_guest()
#         self.assertEqual(0, len(self.room.guests))
#
#     def test_room_can_take_all(self):
#         self.assertEqual(True, self.room.is_big_enough(self.customer))
#
#     def test_room_can_take__all(self):
#         self.assertEqual(False, self.room.is_big_enough(self.customer3))