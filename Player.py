
class Player:
    def __init__(self, current_location=(33.979310, -117.326730)):
        self.current_location = current_location
        self.health = 100
        self.infamy = 1

    def move(self, new_location):
        self.current_location = new_location

    def find_enhancement(self, enhancement):
        self.survival_chance += enhancement