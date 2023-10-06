from datetime import date


class Python:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


sneeky = Python("Sneeky", "domestic python")

print(f"{sneeky.name} is a {sneeky.species} added on {sneeky.date_added}")
