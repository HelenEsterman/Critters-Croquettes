from datetime import date


class Shark:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


bruce = Shark("Bruce", "domestic shark")

print(f"{bruce.name} is a {bruce.species} added on {bruce.date_added}")