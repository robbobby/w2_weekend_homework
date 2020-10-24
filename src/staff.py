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
