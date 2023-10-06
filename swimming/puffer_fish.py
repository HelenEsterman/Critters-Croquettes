from datetime import date


class PufferFish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


snoop_dogg = PufferFish("Snoop Dogg", "domestic puffer fish")

print(f"{snoop_dogg.name} is a {snoop_dogg.species} added on {snoop_dogg.date_added}")
