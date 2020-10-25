import unittest
from src.customer import *


class TestCustomer(unittest.TestCase):
    def setUp(self):
        # 1name, 2age, 3fun_level, 4thirst, 5hunger, 6wants_alcohol, 7atmosphere, 8happy, 9partner, 10wallet
        self.customer = Customer("Jeff", 24, 80, 70, 60, 10, 0, 90, None, 100)
        self.customer2 = Customer("Margaret", 15, 83, 70, 99, 10, 0, 90, self.customer, 200)
        self.customer3 = Customer("Dorothy", 47, 83, 70, 99, 10, 0, 90, None, 200)
        self.customer4 = Customer("Humphrey", 15, 83, 70, 14, 10, 0, 90, None, 200)

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