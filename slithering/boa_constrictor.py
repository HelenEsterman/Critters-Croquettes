from datetime import date


class BoaConstrictor:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


wayne = BoaConstrictor("Wayne", "domestic boa constrictor")

print(f"{wayne.name} is a {wayne.species} added on {wayne.date_added}")
