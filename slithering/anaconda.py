from datetime import date


class Anaconda:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


nincki_minjaje = Anaconda("Nincki Minjaje", "domestic anaconda")

print(f"{nincki_minjaje.name} is a {nincki_minjaje.species} added on {nincki_minjaje.date_added}")
