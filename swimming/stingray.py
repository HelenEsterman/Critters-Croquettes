from datetime import date


class Stingray:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


sting = Stingray("Sting", "domestic stingray")

print(f"{sting.name} is a {sting.species} added on {sting.date_added}")
