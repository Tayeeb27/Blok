###Class for creating containers for storing in-game items such as cupboards, drawers, wardrobes, desks, etc.
from random_code import *
class container:
    def __init__(self, id, name, contents, description=None, locked=False, access_code=None):
        self.id = id               # ID of the container
        self.name = name           # Name of the container
        self.contents = contents   # [item1,item2,item3]
        self.description = description
        self.locked = locked
        self.access_code = access_code
        
    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)
            return True
        return False
    
    def add_item(self,item):
        self.contents.append(item)
    
    def print_description(self):
        print(f"\n{self.name.upper()}\n{self.description}")


##CREATE CONTAINERS BELOW###

# containerID = container(id, name, contents, OPTIONAL description)

containers = {"wardrobe_room1": container("wardrobe_room1", "Wardrobe", ["item_book", "item_shoes"], "Old wooden wardrobe"),
              "desk_room2": container("desk_room2", "Desk", ["item_facemask","item_pink_slip"], "Wooden desk"),
              "safe_room2": container("safe_room2", "Safe", ["item_keycard"], "A code-locked safe.", True, generate_code()),
              "safe_room4_floor_1": container("safe_room2_floor_1", "Safe", ["item_master_keycard"], "A code-locked safe", True, ceaser_cipher()),
              }