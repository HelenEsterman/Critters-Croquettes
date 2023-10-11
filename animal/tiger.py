from movements.walking import Walking
from .animals import Animal


class Tiger(Animal, Walking):

    def __init__(self, name, species, food, chip_num, shift):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift
        Walking.__init__(self)
