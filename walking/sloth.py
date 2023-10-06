from datetime import date


class Sloth:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


dash = Sloth("Dash", "domestic sloth")

print(f"{dash.name} is a {dash.species} added on {dash.date_added}")
