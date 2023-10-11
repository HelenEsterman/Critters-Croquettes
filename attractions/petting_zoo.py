from .attraction import Attraction


class PettingZoo(Attraction):

    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)

    def add_animal(self, animal):
        try:
            if hasattr(animal, 'walk_speed'):
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError:
            print(
                f'{animal.name} does not like to be petted, it cannot live in {self.attraction_name}')
