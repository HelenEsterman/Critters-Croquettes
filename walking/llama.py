from datetime import date


class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


miss_fuzz = Llama("Miss Fuzz", "domestic llama")

print(f"{miss_fuzz.name} is a {miss_fuzz.species} added on {miss_fuzz.date_added}")
