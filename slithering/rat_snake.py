from datetime import date


class RatSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


remy = RatSnake("Remy", "domestic rat snake")

print(f"{remy.name} is a {remy.species} added on {remy.date_added}")
