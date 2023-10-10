from animal.animals import Animal


class Tiger(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
