from movements.swimming import Swimming
from .animals import Animal


class Shark(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
