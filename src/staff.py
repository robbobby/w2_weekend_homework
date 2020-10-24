from src.food_ability import FoodAbility

class Staff:
    def __init__(self, name, tiredness, age, skill, job, food_ability):
        self.job = job
        self.food_ability = food_ability
        self.skill = skill
        self.age = age
        self.tiredness = tiredness
        self.name = name

    def make_older(self):
        self.age +=1

    def increase_skill(self, increase_by):
        self.skill += increase_by

    def decrease_skill(self, decrease_by):
        if self.skill - decrease_by > 0:
            self.skill -= decrease_by
        else:
            self.skill = 0

    def change_job(self, job):
        self.job = job

    def has_food_ability(self, food):
        for ability in self.food_ability:
            if ability == food:
                return True

        return False

    def remove_food_ability(self, food):
        for ability in self.food_ability:
            if ability == food:
                self.food_ability.remove(ability)

    def add_ability(self, food):
        if not self.has_food_ability(food):
            self.remove_food_ability(FoodAbility.NONE)
            self.food_ability.append(food)
