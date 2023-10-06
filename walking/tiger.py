from datetime import date


class Tiger:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


shere_khan = Tiger("Shere Khan", "domestic tiger")

print(f"{shere_khan.name} is a {shere_khan.species} added on {shere_khan.date_added}")
