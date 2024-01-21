from functions import print_story
from functions import generate_survival_chance
from Player import Player

print_story()

player = Player()

i = 0
while i < 5:        # loop reflects the chance of survival for 5 prompted locations to move to
    print(generate_survival_chance(player))
    i += 1