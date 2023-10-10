class Attraction:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        return self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]
