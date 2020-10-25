import unittest

from src.Room.bath import Bath
from src.Room.bathroom import Bathroom
from src.Room.room import Room
from src.Room.room_types import RoomType
from src.Room.sink import Sink
from src.Room.toilet import Toilet
from src.customer import *
from src.dukebox import DukeBox
from src.genre import Genre
from src.song import Song


class TestCustomer(unittest.TestCase):
    def setUp(self):

                                ##### Customer Set Up #####
        # 1name, 2age, 3fun_level, 4thirst, 5hunger, 6wants_alcohol, 7atmosphere, 8happy, 9partner, 10wallet
        self.customer = Customer("Jeff", 24, 80, 70, 60, 10, 0, 90, None, 100)
        self.customer2 = Customer("Margaret", 15, 83, 70, 99, 10, 0, 90, self.customer, 200)
        self.customer3 = Customer("Dorothy", 47, 83, 70, 99, 10, 0, 90, None, 200)
        self.customer4 = Customer("Humphrey", 15, 83, 70, 14, 10, 0, 90, None, 200)


                                ##### Room Set Up #####
        self.bath = Bath("Bath Extra", 7, 100, 10)
        self.toilet = Toilet("ToLet Amaze", 7, 100, 10)
        self.sink = Sink("sink Extra", 7, 100, 10)

        self.song = [Song("Cafo", "Animals as Leaders", 2009, Genre.ALTERNATIVE_METAL),
                     Song("Electric Sunrise", "Plini", 2016, Genre.PROG_METAL),
                     Song("Pastures", "Plini", 2016, Genre.PROG_METAL)]

        self.dukebox = DukeBox(self.song, 99, [])

        self.room = Room([], self.dukebox, RoomType.DELUXE)

        self.bathroom = Bathroom(self.sink, self.bath, self.toilet, self.room.room_quality)



    def test_customer_has_name(self):
        self.assertEqual("Jeff", self.customer.name)

    def test_customer_has_age(self):
        self.assertEqual(24, self.customer.age)

    def test_customer_has_fun_level(self):
        self.assertEqual(80, self.customer.fun_level)

    def test_customer_has_thirst(self):
        self.assertEqual(70, self.customer.thirst)

    def test_customer_has_hunger(self):
        self.assertEqual(60, self.customer.hunger)

    def test_customer_has_want_alcohol(self):
        self.assertEqual(10, self.customer.wants_alcohol)

    def test_customer_has_atmosphere(self):
        self.assertEqual(0, self.customer.atmosphere)

    def test_customer_has_happy(self):
        self.assertEqual(90, self.customer.happy)

    def test_customer_has_partner(self):
        self.assertEqual(self.customer, self.customer2.partner)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_joint_wallet(self):
        self.assertEqual(300, self.customer2.get_joint_wallet())

    def test_set_partner_on_init(self):  ## called on init ##
        # self.customer.set_partner(self.customer2)
        self.assertEqual(self.customer2, self.customer.partner)

    def test_add_to_longs_for(self):
        self.customer.add_to_longs_for(self.customer)
        self.assertEqual("Jeff", self.customer.longs_for[0].name)

    def test_remove_partners_partner(self):
        self.customer.remove_self_from_partner()
        self.assertEqual(None, self.customer2.partner)

    def test_remove_partner(self):
        self.customer2.remove_partner()
        self.assertEqual(None, self.customer2.partner)

    def test_set_new_partner(self):
        self.customer.set_partner(self.customer3)
        self.assertEqual(self.customer3, self.customer.partner)

    def test_set_customer_room(self):
        self.customer.set_room(self.room)
        self.assertEqual(self.room, self.customer.room)

    def test_set_customers_partner_room(self):
        self.customer.set_room(self.room)
        self.assertEqual(self.room, self.customer2.room)

    def test_remove_customers_room(self):
        self.customer.remove_room()
        self.assertEqual(None, self.customer.room)

    def test_remove_customers_partners_room(self):
        self.customer.remove_room()
        self.assertEqual(None, self.customer2.room)

    def test_check_has_money(self):
        self.assertEqual(True, self.customer.has_money(50))

    def test_check_has__money(self):
        self.assertEqual(False, self.customer.has_money(150))

    def test_add_money(self):
        self.customer.add_money(20)
        self.assertEqual(120, self.customer.wallet)

    def test_take_money(self):
        self.customer.take_money(20)
        self.assertEqual(80, self.customer.wallet)

    def test_take__money(self):
        self.customer.take_money(120)
        self.assertEqual(100, self.customer.wallet)

    def test_borrow_money(self):
        self.customer.borrow_money(20)
        self.assertEqual(120, self.customer.wallet)
        self.assertEqual(180, self.customer2.wallet)

    def test_borrow___money(self):
        self.customer.borrow_money(250)
        self.assertEqual(100, self.customer.wallet)
        self.assertEqual(200, self.customer2.wallet)

    def test_borrow__money(self):
        self.customer3.borrow_money(20)
        self.assertEqual(200, self.customer3.wallet)
