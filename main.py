from functions import print_story
from functions import generate_survival_chance
from Player import Player
from nearbysearch import print_one_place
from functions import generate_health_bonus

print_story()

player = Player()

#while player.health > 0:        # while player is alive
for x in range(5):
        chance = generate_survival_chance(player)
        print(str(chance) + "% survival -> +" + str(generate_health_bonus(chance)) + " hp")
        #print(print_one_place() + str(chance) + " | Cybernetic Enhancement Value: " + str(generate_health_bonus(chance)))
    
    # below code to terminate while loop needs fix
    # player.health = player.health - 25      # to terminate function
    # print(player.health)
    
    