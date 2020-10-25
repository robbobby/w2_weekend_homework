class BathroomUtility:
        def __init__(self, model, comfort, hygiene, atmosphere_level):
            self.model = model
            self.atmosphere_level = atmosphere_level
            self.comfort = comfort
            self.hygiene = hygiene
            self.max_atmosphere = atmosphere_level

        def clean(self):
            self.hygiene = 100

        def set_atmosphere(self):
            self.atmosphere_level = self.hygiene * self.max_atmosphere // 100