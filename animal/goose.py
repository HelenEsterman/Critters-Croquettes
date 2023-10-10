from .animals import Animal
from movements.walking import Walking
from movements.swimming import Swimming


class Goose(Animal, Walking, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)

    def honk(self):
        print("The goose honks. A lot")

    def __str__(self):
        return f'{self.name} the Goose'
