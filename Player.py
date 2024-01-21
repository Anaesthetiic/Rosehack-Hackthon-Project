
class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        self.survival_chance = 100

    def move(self, new_location):
        self.current_location = new_location

    def find_enhancement(self, enhancement):
        self.survival_chance += enhancement
        
        
        