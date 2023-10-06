from datetime import date


class Giraffe:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


dottie = Giraffe("Dottie", "domestic giraffe")

print(f"{dottie.name} is a {dottie.species} added on {dottie.date_added}")
