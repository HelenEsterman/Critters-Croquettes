from datetime import date


class RatSnake:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True
