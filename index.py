from slithering import Anaconda, BoaConstrictor, CopperheadSnake, Python, RatSnake
from swimming import FlowerHornFish, Jellyfish, PufferFish, Shark, Stingray
from walking import Donkey, Giraffe, Llama, Sloth, Tiger


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

print(f'{shere_khan.name} the {shere_khan.species} is available to pet during the {shere_khan.shift} shift.')
print(f'{dash.name} the {dash.species} is available to pet during the {dash.shift} shift.')
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(f'{dottie.name} the {dottie.species} is available to pet during the {dottie.shift} shift.')
print(f'{murph.name} the {murph.species} is available to pet during the {murph.shift} shift.')
shere_khan.feed()
