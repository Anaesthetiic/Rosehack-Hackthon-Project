from functions import print_story
from Player import Player

print_story()

def main():
    # Replace with your actual API key
    api_key = 'AIzaSyBdEluVk5_sp43-7fz8iUOw4qdpIKzzytQ'

    # Create a new player
    player = Player("John Doe")
    
    player.display_stats()

    # Keep moving until the user decides to stop
    while True:
        # Call the move method
        player.move(api_key)

        # Ask the user if they want to move again
        again = input("Do you want to move again? (yes/no): ")
        if again.lower() != "yes":
            break

        # Display player stats after each move
        player.display_stats()

    # Display player stats when the player decides to stop
    player.display_stats()

if __name__ == "__main__":
    main()