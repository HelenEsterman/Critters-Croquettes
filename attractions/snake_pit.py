class SnakePit:

    def __init__(self, attraction_name, description):

        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self):
        return self.animals.append(self)
