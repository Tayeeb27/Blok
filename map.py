class room:
    def __init__(self, id, name, floor, doors, description, items=[], containers=[], locked=False, explored=False,
                 alias="", npc=None, interactable=True):
        self.id = id  # room ID
        self.name = name  # room name
        self.floor = floor  # floor room is on
        # List of where doors in the current room lead     [room1,room2]
        self.doors = doors
        self.description = description  # room description
        # List of items in the room not in a container [itemID_1, itemID_2]
        self.items = items
        # List of containers IDs in the room  [containerID,containerID2]
        self.containers = containers
        self.locked = locked  # for lift and maintenance rooms
        self.explored = explored  # Stops menu and description being printed multiple times
        self.alias = alias
        self.npc = npc
        self.interactable = interactable


##CREATE ROOMS##

# roomID = room(roomID, room name, {"north":room1, "east":room2, "west":room4}, "EXAMPLE ROOM DESCRIPTION", [])

rooms = {

            # if in exit, commence ending
            "exit_0": room("exit_0", "Exit", 0, [], "You must have all the items.", locked=True),

            "hallway_4": room("hallway_4", "Hallway", 4, ["therapist_office", "lift_4", "bar"],
                              "Top floor of the building", [], [], alias="Floor 4"),
            "hallway_3": room("hallway_3", "Hallway", 3,
                              ["flr3_room_1", "flr3_room_2", "flr3_room_3", "flr3_room_4", "room_maintenance_3",
                               "lift_3"],
                              "Eerie, smelly, and damp.\nLooks like a few rooms.\nSeems to have a staircase, but it's "
                              "blocked...\nIs that a lift?!", alias="Floor 3"),
            "hallway_2": room("hallway_2", "Hallway", 2,
                              ["flr2_room_1", "flr2_room_2", "flr2_room_3", "flr2_room_4", "room_security", "lift_2"],
                              "The security room!\nThere might be some answers in there.", alias="Floor 2"),
            "hallway_1": room("hallway_1", "Hallway", 1,
                              ["flr1_room_1", "flr1_room_2", "flr1_room_3", "flr1_room_4", "room_maintenance_1",
                               "lift_1"], "Scary, rank, and clammy.\nThis hallway looks like it never ends.",
                              alias="Floor 1"),
            "hallway_0": room("hallway_0", "Hallway", 0, ["lift_0", "exit_0"], "Congratulations, you can now leave.",
                              alias="Floor 0"),

            "lift_0": room("lift_0", "Lift", 0, ["hallway_3", "hallway_2", "hallway_1"], "Almost there...",
                           locked=True),
            "lift_4": room("lift_4", "Lift", 4, ["hallway_3", "hallway_2", "hallway_1"], "Looks like you need "
                                                                                         "some sort of card?",
                           locked=False),

            "lift_3": room("lift_3", "Lift", 3, ["hallway_3", "hallway_2", "hallway_1"], "Looks like you need "
                                                                                         "some sort of card?",
                           locked=True),
            "lift_2": room("lift_2", "Lift", 2, ["hallway_3", "hallway_2", "hallway_1"], "Looks like you need "
                                                                                         "some sort of card?",
                           locked=True),
            "lift_1": room("lift_1", "Lift", 1, ["hallway_3", "hallway_2", "hallway_1"], "Looks like you need "
                                                                                         "some sort of card?",
                           locked=True),

            "bar": room("bar", "Bar", 5, ["hallway_4"], "Private bar, Facemask and Members card needed for entry",
                        locked=True),


            "therapist_office": room("therapist_office", "Therapy", 4, ["hallway_4"],
                                     "Your therapists office.", alias="Therapist", npc="therapist", locked=True),


            # unlocked until lockpicking works
            "room_power_3": room("room_power_3", "power room", 3, ["hallway_3"],
                                 "Seems to need a key...\nMaybe you can use something to pick the lock?", locked=True,
                                 alias="Power"),
            "room_maintenance_3": room("room_maintenance_3", "maintenance room", 3, ["hallway_3", "room_power_3"],
                                       "Maintenance & Power Room.", locked=False, alias="Maintenance"),

            "room_security": room("room_security", "Security room", 2, ["hallway_2"], "Seems like a CCTV/Security Room",
                                  [], locked=True, alias="Security"),
            "room_maintenance_1": room("room_maintenance_1", "maintenance room", 1, ["hallway_1"],
                                       "Description of maintenance Room", alias="Maintenance"),

            "flr1_room_1": room("flr1_room_1", "Room 1", 1, ["hallway_1"],
                                "You notice how this room perfectly resembles the "
                                "room in which you woke up in.\nThe wardrobe and "
                                "bed both placed in the exact same spot.\nIsn't "
                                "that strange...",
                                ["item_note_cipher_key"],
                                ["wardrobe_room1"], alias="1"),
            "flr1_room_2": room("flr1_room_2", "Room 2", 1, ["hallway_1"], "The doors have been wrapped in chains,\n"
                                                                           "effectively preventing any way of opening them by "
                                                                           "a usable margin.\nYou push the doorknob but the "
                                                                           "chains bind the doors tightly like a leash on a "
                                                                           "dog’s collar. ", [],
                                alias="2", interactable=False),

"flr1_room_3": room("flr1_room_3", "Room 3", 1, ["hallway_1"], "This door seemed familiar.\nLike you had been "
                                                               "here before.\nAs you enter you see a woman "
                                                               "rearranging her shelf decorations. ",["item_scrap4"], alias="3", npc="hannah"),

"flr1_room_4": room("flr1_room_4", "Room 4", 1, ["hallway_1"], "The entryway squeaks as you venture inside.\nYou "
                                                               "feel a sharp breeze as the lifeless aroma "
                                                               "surrounds you.", ["item_note_cipher",
                                                                                  "item_vial"],
                    ["safe_room4_floor_1"], alias="4"),

"flr2_room_1": room("flr2_room_1", "Room 1", 2, ["hallway_2"], "Peters apartment.\nIt is a small and packed place "
                                                               "with plenty of books and plants. It is quite "
                                                               "cozy.", ["item_scrap2"], alias="1", npc="peter"),

"flr2_room_2": room("flr2_room_2", "Room 2", 2, ["hallway_2"], "As you enter you notice the potent stench of "
                                                               "cannabis. A cluster of used needles lay beside an "
                                                               "old, worn out mattress. ", ["item_shirt",
                                                                                            "item_bar_card",
                                                                                            "item_scrap3"], [],
                    alias="2", npc="magpie"),
"flr2_room_3": room("flr2_room_3", "Room 3", 2, ["hallway_2"], "You try to touch the door handle but your hand "
                                                               "seems to have passed through it and landed on a "
                                                               "brick wall.\nYes, there is certainly no door "
                                                               "handle, as well as the actual door.\nIt seems to "
                                                               "have been painted on the brick wall for some "
                                                               "reason.\nBudget cuts, relationship issues, "
                                                               "debt? \nNo question to be found here.", alias="3"),
"flr2_room_4": room("flr2_room_4", "Room 4", 2, ["hallway_2"], "The doors have been blocked by two diagonally "
                                                               "crossed planks of wood firmly attached to the "
                                                               "walls and the doors themself. As solid as things "
                                                               "can be.", alias="4", interactable=False),
"flr3_room_1": room("flr3_room_1", "Room 1", 3, ["hallway_3"],
                    "A bedroom, you wake up half-naked, with a bad case of amnesia...\nThere's a fork sticking a "
                    "note into the wall?", ["item_note_1", "item_fork"],
                    ["wardrobe_room1"], alias="1"),
"flr3_room_2": room("flr3_room_2", "Room 2", 3, ["hallway_3"], "Seems like a drug den... ",
                    ["item_baggy"], ["desk_room2", "safe_room2"], alias="2"),
"flr3_room_3": room("flr3_room_3", "Room 3", 3, ["hallway_3"], "The air in the room turned out to be abruptly "
                                                               "cold. There was a feeling of overpowering trouble "
                                                               "and fear.\nThe room appeared to take on its very "
                                                               "own existence. So miserable, so irate, "
                                                               "and cold. ", ["item_note_3", "item_scrap1",
                                                                              "item_lipstick"], alias="3"),
"flr3_room_4": room("flr3_room_4", "Room 4", 3, ["hallway_3"], "There is a metal bar on two hinges seeming to "
                                                               "prevent opening of the doors.\nYou carefully "
                                                               "remove it and put it next to the doors.\nAfter "
                                                               "opening the room you see the entire apartment "
                                                               "filled to the brim with mannequins,\nthey fill in "
                                                               "the entire space without any gaps whatsoever - "
                                                               "just a solid wall of plastic bodies seemingly "
                                                               "melted into each other.\nYou feel a sense of dread "
                                                               "in this picture and get out of the room,\n"
                                                               "closing the room and locking it with the bar.",
                    alias="4", interactable=False)
}
