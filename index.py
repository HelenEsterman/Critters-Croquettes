from slithering import Anaconda, BoaConstrictor, CopperheadSnake, Python, RatSnake
from swimming import FlowerHornFish, Jellyfish, PufferFish, Shark, Stingray
from walking import Donkey, Giraffe, Llama, Sloth, Tiger
from attractions import PettingZoo, SnakePit, Wetlands


shere_khan = Tiger("Shere Khan", "domestic tiger", "morning", "raw beef")
dash = Sloth("Dash", "domestic sloth", "midday", "eucalyptus")
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "afternoon", "llama chow")
dottie = Giraffe("Dottie", "domestic giraffe", "morning", "leaves")
murph = Donkey("Murph", "domestic donkey", "afternoon", "donkey chow")
sting = Stingray("Sting", "domestic stingray", "clams")
bruce = Shark("Bruce", "domestic shark", "catfish")
snoop_dogg = PufferFish("Snoop Dogg", "domestic puffer fish", "mussels")
genie = Jellyfish("Genie", "domestic jellyfish", "oysters")
pudge = FlowerHornFish("Pudge", "domestic flower horn fish", "fish pellets")
remy = RatSnake("Remy", "domestic rat snake", "frozen mice")
sneeky = Python("Sneeky", "domestic python", "live mice")
penny = CopperheadSnake("Penny", "domestic copperhead snake", "frozen mice")
wayne = BoaConstrictor("Wayne", "domestic boa constrictor", "live mice")
nincki_minjaje = Anaconda("Nincki Minjaje", "domestic anaconda", "live mice")

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

varmint_list = ""

for animal in varmint_village.animals:
    varmint_list += f"""
{animal.name} the {animal.species}"""

print(f"""{varmint_village.attraction_name} is where you'll find {varmint_village.description} like, {varmint_list}""")

critter_list = ""

for animal in critter_cove.animals:
    critter_list += f"""
{animal.name} the {animal.species}"""

print(f"""{critter_cove.attraction_name} is where you'll find {critter_cove.description} like, {critter_list}""")

slither_list = ""

for animal in slither_inn.animals:
    slither_list += f"""
{animal.name} the {animal.species}"""

print(f"""{slither_inn.attraction_name} is where you'll find {slither_inn.description} like, {slither_list}""")
