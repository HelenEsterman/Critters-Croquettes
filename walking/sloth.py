from datetime import date


class Sloth:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
