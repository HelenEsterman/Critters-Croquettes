from datetime import date


class CopperheadSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


penny = CopperheadSnake("Penny", "domestic copperhead snake")

print(f"{penny.name} is a {penny.species} added on {penny.date_added}")
