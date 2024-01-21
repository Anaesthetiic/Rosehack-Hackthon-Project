from nearbysearch import get_places_nearby
import random
class Player:
    def __init__(self, current_location=(33.979310, -117.326730)):
        self.current_location = current_location
        self.health = 100
        self.infamy = 1

    def move(self, api_key):
        while True:
            # Get a list of nearby places
            places = get_places_nearby(api_key, ','.join(map(str, self.current_location)), '32186.9')

            # Select 5 random places
            places = random.sample(places, 5)

            # Print the place names and ask the player to choose one
            print("Choose a place to move to:")
            for i, place in enumerate(places, start=1):
                print(f"{i}. {place['name']}")

            choice = int(input("Enter the number of your choice: ")) - 1

            # Update the player's location to the chosen place
            self.current_location = places[choice]['coordinates']
            
            print(f"You have moved to {places[choice]['name']}.")

            # Ask the player if they want to move again
            again = input("Do you want to move again? (yes/no): ")
            if again.lower() != "yes":
                break
        

    def find_enhancement(self, enhancement):
        self.survival_chance += enhancement