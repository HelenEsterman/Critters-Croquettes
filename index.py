from slithering import Anaconda, BoaConstrictor, CopperheadSnake, Python, RatSnake
from swimming import FlowerHornFish, Jellyfish, PufferFish, Shark, Stingray
from walking import Donkey, Giraffe, Llama, Sloth, Tiger


shere_khan = Tiger("Shere Khan", "domestic tiger", "morning")
dash = Sloth("Dash", "domestic sloth", "midday")
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "afternoon")
dottie = Giraffe("Dottie", "domestic giraffe", "morning")
murph = Donkey("Murph", "domestic donkey", "afternoon")
sting = Stingray("Sting", "domestic stingray")
bruce = Shark("Bruce", "domestic shark")
snoop_dogg = PufferFish("Snoop Dogg", "domestic puffer fish")
genie = Jellyfish("Genie", "domestic jellyfish")
pudge = FlowerHornFish("Pudge", "domestic flower horn fish")
remy = RatSnake("Remy", "domestic rat snake")
sneeky = Python("Sneeky", "domestic python")
penny = CopperheadSnake("Penny", "domestic copperhead snake")
wayne = BoaConstrictor("Wayne", "domestic boa constrictor")
nincki_minjaje = Anaconda("Nincki Minjaje", "domestic anaconda")

print(f'{shere_khan.name} the {shere_khan.species} is available to pet during the {shere_khan.shift} shift.')
print(f'{dash.name} the {dash.species} is available to pet during the {dash.shift} shift.')
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(f'{dottie.name} the {dottie.species} is available to pet during the {dottie.shift} shift.')
print(f'{murph.name} the {murph.species} is available to pet during the {murph.shift} shift.')
