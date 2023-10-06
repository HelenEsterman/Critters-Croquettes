from datetime import date


class Jellyfish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


genie = Jellyfish("Genie", "domestic jellyfish")

print(f"{genie.name} is a {genie.species} added on {genie.date_added}")
