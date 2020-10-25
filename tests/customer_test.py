import unittest
from src.customer import *


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jeff", 24, 80, 70, 60, 10, 0, 90, None, 100)
        self.customer2 = Customer("Margaret", 15, 80, 70, 60, 10, 0, 90, self.customer, 200)

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
        self.assertEqual(10, self.customer.wants_alhohol)

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

    def test_set_partner(self): ## called on init ##
        # self.customer.set_partner(self.customer2)
        self.assertEqual(self.customer2, self.customer.partner)
