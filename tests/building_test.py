import unittest

from src.Bar.drink import Drink
from src.Bar.food import Food
from src.Room.bath import Bath
from src.Room.bathroom import Bathroom
from src.Room.room import Room
from src.Room.room_types import RoomType
from src.Room.sink import Sink
from src.Room.toilet import Toilet
from src.building import *
from src.customer import Customer
from src.dukebox import DukeBox
from src.Bar.bar import Bar
from src.food_ability import FoodAbility
from src.genre import Genre
from src.song import Song
from src.staff import Staff
from src.staff_jobs import Job


class TestBuilding(unittest.TestCase):
    def setUp(self):

                                ##### Staff #####
        self.staff = [Staff("Bob", 1, 21, 4, Job.CHEF, [FoodAbility.CHINESE]),
                      Staff("Barbera", 10, 92, 4, Job.DOORMAN, [FoodAbility.INDIAN]),
                      Staff("George", 100, 12, 4, Job.CHEF, [FoodAbility.NONE]),
                      Staff("Margery", 100, 30, 4, Job.BARMAN, [FoodAbility.NONE])
                      ]

                                ##### Drinks #####
        self.wine = Drink("Wine", 899, 67)
        self.cola = Drink("Cola", 199, 0)
        self.vodka = Drink("Vodka", 299, 0)

                                ##### Food #####
        self.food = Food("Soup", 399, 2, None)
        self.food_1 = Food("Curry", 399, 2, FoodAbility.INDIAN)
        self.food_not = Food("Chinese", 899, 2, FoodAbility.CHINESE)

                                ##### Songs #####
        self.song = [Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL),
                     Song("Electric Sunrise", "Plini", 2016, Genre.PROG_METAL),
                     Song("Pastures", "Plini", 2016, Genre.PROG_METAL)]

                                ##### Duke Box #####
        self.dukebox = DukeBox(self.song, 99, [])

                                ##### Bar #####
        self.bar = Bar(self.dukebox, [self.staff[0], self.staff[3]], [self.cola, self.wine],
                       [self.food, self.food_1])

        self.bar.drinks_list[0].add_stock(60)
        self.bar.drinks_list[1].add_stock(90)
        self.bar.food_list[0].add_stock(100)
        self.bar.food_list[1].add_stock(70)

                                ##### Bathroom #####

        self.bath = Bath("Bath Extra", 7, 100, 10)
        self.toilet = Toilet("ToLet Amaze", 7, 100, 10)
        self.sink = Sink("sink Extra", 7, 100, 10)

        self.bathroom = Bathroom(self.sink, self.bath, self.toilet, None)

                                ##### Rooms #####
        self.rooms = [Room([self.bathroom], self.dukebox, RoomType.SINGLE),
                      Room([self.bathroom], self.dukebox, RoomType.DOUBLE),
                      Room([self.bathroom], self.dukebox, RoomType.TRIPLE),
                      Room([self.bathroom], self.dukebox, RoomType.DELUXE)
                      ]

                                ##### Customers #####

        self.customers = [Customer("Jeff", 24, 80, 70, 60, 10, 0, 90, None, 100),
                          Customer("Margaret", 15, 83, 70, 99, 10, 0, 90, None, 200),
                          Customer("Dorothy", 47, 83, 70, 99, 10, 0, 90, None, 200),
                          Customer("Humphrey", 15, 83, 70, 14, 10, 0, 90, None, 200)
        ]
        self.customers[1].set_partner(self.customers[0])

                                ##### Building #####
        self.building = Building(self.rooms, self.bar, self.customers, self.staff)

    def test_building_has_bar(self):
        self.assertEqual(self.bar, self.building.bar)

    # def test_rooms_have_atmosphere(self):
    #     self.assertEqual(22, self.building.rooms[0].atmosphere) ## Not working correctly

    def test_building_has_duke_box(self):
        self.assertEqual(self.dukebox, self.building.bar.dukebox)

    def test_building_has_staff(self):
        self.assertEqual(self.staff[0], self.building.staff[0])

    def test_building_has_own_wallet(self):
        self.assertEqual(200000, self.building.wallet)

