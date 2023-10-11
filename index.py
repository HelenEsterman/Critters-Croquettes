from animal import Anaconda, BoaConstrictor, CopperheadSnake, Python, RatSnake, FlowerHornFish, Jellyfish, PufferFish, Shark, Stingray, Donkey, Giraffe, Llama, Sloth, Tiger, Goose
from attractions import PettingZoo, SnakePit, Wetlands


shere_khan = Tiger("Shere Khan", "domestic tiger", "raw beef", 123, "morning")
dash = Sloth("Dash", "domestic sloth", "eucalyptus", 124, "midday")
miss_fuzz = Llama("Miss Fuzz", "domestic llama",
                  "llama chow", 125, "afternoon")
dottie = Giraffe("Dottie", "domestic giraffe", "leaves", 126, "morning")
murph = Donkey("Murph", "domestic donkey", "donkey chow", 127, "afternoon")
sting = Stingray("Sting", "domestic stingray", "clams", 128)
bruce = Shark("Bruce", "domestic shark", "catfish", 129)
snoop_dogg = PufferFish("Snoop Dogg", "domestic puffer fish", "mussels", 130)
genie = Jellyfish("Genie", "domestic jellyfish", "oysters", 134)
pudge = FlowerHornFish(
    "Pudge", "domestic flower horn fish", "fish pellets", 135)
remy = RatSnake("Remy", "domestic rat snake", "frozen mice", 136)
sneeky = Python("Sneeky", "domestic python", "live mice", 137)
penny = CopperheadSnake(
    "Penny", "domestic copperhead snake", "frozen mice", 138)
wayne = BoaConstrictor("Wayne", "domestic boa constrictor", "live mice", 139)
nincki_minjaje = Anaconda(
    "Nincki Minjaje", "domestic anaconda", "live mice", 140)
juice = Goose("Juice", "domestic goose", "fish", 150)

slither_inn = SnakePit(
    "The Slither Inn", "houses more snakes than an Indiana Jones movie")
critter_cove = Wetlands(
    "Critter Cove", "full of feathered friends and fantastic fish")
varmint_village = PettingZoo(
    "Varmint Village", "outdoor corral of friendly four-legged critters looking for a pat on the head and a handful of treats")

print(f'{shere_khan.name} the {shere_khan.species} is available to pet during the {shere_khan.shift} shift.')
print(f'{dash.name} the {dash.species} is available to pet during the {dash.shift} shift.')
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(f'{dottie.name} the {dottie.species} is available to pet during the {dottie.shift} shift.')
print(f'{murph.name} the {murph.species} is available to pet during the {murph.shift} shift.')
shere_khan.feed()
dash.feed()
remy.feed()
print(shere_khan)
print(dash)
print(snoop_dogg)
print(penny)

varmint_village.add_animal(shere_khan)
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(dash)
varmint_village.add_animal(dottie)
varmint_village.add_animal(murph)
# print(varmint_village.animals)
critter_cove.add_animal(sting)
critter_cove.add_animal(bruce)
critter_cove.add_animal(snoop_dogg)
critter_cove.add_animal(genie)
critter_cove.add_animal(pudge)
# print(critter_cove.animals)
slither_inn.add_animal(remy)
slither_inn.add_animal(sneeky)
slither_inn.add_animal(penny)
slither_inn.add_animal(wayne)
slither_inn.add_animal(nincki_minjaje)
# print(slither_inn.animals)

# varmint_list = ""

# for animal in varmint_village.animals:
#     varmint_list += f"""
# {animal.name} the {animal.species}"""

# print(f"""{varmint_village.attraction_name} is where you'll find {varmint_village.description} like, {varmint_list}""")

# critter_list = ""

# for animal in critter_cove.animals:
#     critter_list += f"""
# {animal.name} the {animal.species}"""

# print(f"""{critter_cove.attraction_name} is where you'll find {critter_cove.description} like, {critter_list}""")

# slither_list = ""

# for animal in slither_inn.animals:
#     slither_list += f"""
# {animal.name} the {animal.species}"""

# print(f"""{slither_inn.attraction_name} is where you'll find {slither_inn.description} like, {slither_list}""")


print(miss_fuzz)
miss_fuzz_dict = vars(miss_fuzz)

for key in miss_fuzz_dict.keys():
    print(f"{key}: {miss_fuzz_dict[key]}")


sleepy = Sloth("Sleepy", "domestic sloth", "eucalyptus", 12345, "midday")
print(sleepy.name)
sleepy.name = "Changed"
sleepy.chip_num = 845
print(sleepy.chip_num)
print(sleepy.name)

print(slither_inn.last_critter_added)
print(varmint_village.last_critter_added)
print(critter_cove.last_critter_added)

miss_fuzz.feed()
shere_khan.feed()
print(shere_khan)
print(juice)
juice.walk()
juice.swim()

varmint_village.add_animal(juice)

for animal in varmint_village.animals:
    print(animal)


varmint_village.add_animal(sting)
varmint_village.add_animal(shere_khan)
varmint_village.add_animal(dash)
varmint_village.add_animal(sleepy)
print(varmint_village.animals)

for animal in varmint_village.animals:
    print(animal)
