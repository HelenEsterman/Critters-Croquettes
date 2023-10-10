from animal.animals import Animal
from datetime import date


class Llama(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def feed(self):
        print(
            f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')
