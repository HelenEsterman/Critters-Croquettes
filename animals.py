# import the python datetime module to help us create a timestamp
"""_animals_"""
from datetime import date


class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()


miss_fuzz = Llama("Miss Fuzz", "domestic llama")
# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"

llama_dictionary = []
llama_dictionary.append(miss_fuzz)
print(llama_dictionary)


# for key in llama_dictionary.keys():
#     print(f"{key}: {llama_dictionary[key]}")
