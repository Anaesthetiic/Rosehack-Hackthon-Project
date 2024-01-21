import random
import Player

def print_story():
        print("It's the year 2142, AI has taken over the world. All humans are now being hunted and killed.")
        print("This game is simple. You will start off in Riverside County and be given a choice whether to travel to a different county or stay.")
        print("You can only travel a maximum of 25 miles at a time.")
        print("You will be given the population of each county in your vicinity. It is up to you whether you want to move to a different one or not")
        print("If you choose to stay, the likeliness of you being found by the AI will increase.")
        print("If you choose to move, the likeliness of you being found by the AI will decrease if the population of the county is lower than the one you're in.")
        print("You also have the chance to find cybernetic enhancements in each county. That will increase your chances of survival.")
        print("You begin at University of California, Riverside in the Aberdeen-Inverness dorms.")
        print("Good luck, May your survival be long and your death be swift.")
        
def generate_survival_chance(player):
    # Calculate the mean based on the infamy value
    mean = 90 - 10 * player.infamy  # Adjusted mean based on infamy
    
    # Generate a random number with a normal distribution
    number = int(random.gauss(mean, 20))  # Standard Deviation=20
    
    # Ensure the number is within the desired range [0, 100]
    number = max(0, min(100, number))
    
    return number

def generate_health_bonus(survivalChance):
   # Ensure the parameter is within the desired range [0, 100]
    survivalChance = max(0, min(100, survivalChance))

    # Calculate the semi-random number based on the parameter
    generated_number = int((100 - survivalChance) / 100 * 33)
    return generated_number