from datetime import date


class FlowerHornFish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


pudge = FlowerHornFish("Pudge", "domestic flower horn fish")

print(f"{pudge.name} is a {pudge.species} added on {pudge.date_added}")
