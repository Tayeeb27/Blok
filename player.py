class Player:
    def __init__(self, location="flr3_room_1", inventory=[]):
        self.location = location
        self.inventory = inventory

    def move(self, location):
        self.location = location

    def drop(self, item):
        self.inventory.remove(item)

    def pick_up(self, item):
        self.inventory.append(item)
