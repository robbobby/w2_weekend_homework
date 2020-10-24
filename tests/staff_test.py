import unittest
from src.staff import *
from src.food_ability import FoodAbility
from src.staff_jobs import Job


class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff_member = Staff("Bob", 1, 21, 4, Job.CHEF, [FoodAbility.CHINESE])
        self.staff_member2 = Staff("Barbera", 10, 92, 4, Job.DOORMAN, [FoodAbility.INDIAN])
        self.staff_member3 = Staff("George", 100, 12, 4, Job.CHEF, [FoodAbility.NONE])

    def test_staff_have_name(self):
        self.assertEqual("Bob", self.staff_member.name)

    def test_staff_have___name(self):
        self.assertEqual("George", self.staff_member3.name)

    def test_staff_have_tiredness_level(self):
        self.assertEqual(10, self.staff_member2.tiredness)

    def test_staff_have_tiredness__level(self):
        self.assertEqual(100, self.staff_member3.tiredness)

    def test_staff_have_age(self):
        self.assertEqual(21, self.staff_member.age)

    def test_staff_have__age(self):
        self.assertEqual(92, self.staff_member2.age)

    def test_staff_have_job(self):
        self.assertEqual(Job.DOORMAN, self.staff_member2.job)

    def test_staff__have_job(self):
        self.assertEqual(Job.CHEF, self.staff_member3.job)

    def test_staff_have_food_ability(self):
        self.assertEqual(FoodAbility.INDIAN, self.staff_member2.food_ability[0])

    def test_staff_have_food_ability(self):
        self.assertEqual(FoodAbility.NONE, self.staff_member3.food_ability[0])

    def test_make_staff_older(self):
        self.staff_member.make_older()
        self.assertEqual(22, self.staff_member.age)

    def test_increase_skill(self):
        self.staff_member2.increase_skill(2)
        self.assertEqual(6, self.staff_member2.skill)

    def test_decrease_skill(self):
        self.staff_member2.decrease_skill(2)
        self.assertEqual(2, self.staff_member2.skill)

    def test_decrease__skill(self):
        self.staff_member2.decrease_skill(20)
        self.assertEqual(0, self.staff_member2.skill)

    def test_check_person_job(self):
        self.staff_member3.change_job(Job.MUSCIAN)
        self.assertEqual(Job.MUSCIAN, self.staff_member3.job)

    def test_add_food_ability(self):
        self.staff_member3.add_ability(FoodAbility.INDIAN)
        # print(self.staff_member3.food_ability)
        self.assertEqual(FoodAbility.INDIAN, self.staff_member3.food_ability[-1])

    def test_add_food__ability(self):
        self.staff_member.add_ability(FoodAbility.INDIAN)
        # print(self.staff_member.food_ability)
        self.assertEqual(FoodAbility.INDIAN, self.staff_member.food_ability[-1])

    def test_add_food___ability(self):
        self.staff_member2.add_ability(FoodAbility.INDIAN)
        # print(self.staff_member2.food_ability)
        self.assertEqual(FoodAbility.INDIAN, self.staff_member2.food_ability[-1])

    def test_check_for_food_ability(self):
        self.assertEqual(True, self.staff_member2.has_food_ability(FoodAbility.INDIAN))

    def test_check_for_food__ability(self):
        self.assertEqual(False, self.staff_member2.has_food_ability(FoodAbility.CHINESE))

    def test_remove_food_ability(self):
        self.staff_member3.remove_food_ability(FoodAbility.NONE)
        # print(self.staff_member3.food_ability)
        self.assertEqual([], self.staff_member3.food_ability)