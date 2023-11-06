class item:
    def __init__(self, id, name, description=None):
        self.id = id
        self.name = name
        self.description = description


### CREATE ITEMS BELOW ###

# Note items should have ID "item_note_xx" to allow them to be read

items = {
    "item_keycard": item("item_keycard", "Keycard", "This key card enables you to use the lift."),
    "item_facemask": item("item_facemask", "Face Mask", "You can't go outside without this!"),
    "item_fork": item("item_fork", "Fork", "I wonder what this could be used for?"),
    "item_note_1": item("item_note_1", "Note", "note_1.txt"),  # description acts as filename
    "item_wallet": item("item_wallet", "Wallet", "Seems a bit light..."),
    "item_picture": item("item_picture", "Picture", "An older photograph with a black-haired teenager with a rather "
                                                    "stern look on his face with his parents probably. The woman is a "
                                                    "30-ish tall and lanky blonde with a wide smile. The man has "
                                                    "long, black hair and looks slightly older than a woman - he does "
                                                    "not smile or frown but his eyes look rather satisfied with his "
                                                    "current state despite the smile. The handwritten note in the "
                                                    "lower part of the photo reads: “Us, 2035”"),
    "item_ID_card": item("item_ID_card", "ID Card", "Name: John A. Doe\nDOB: 10/11/2015"),
    "item_baggy": item("item_baggy", "Baggy", "A used bag containing some suspicious looking powder..."),
    "item_keys": item("item_keys", "Keys", "Unlocks a door containing a big switch."),
    "item_book": item("item_book", "Book", "Big brain reading time."),
    "item_shoes": item("item_shoes", "Shoes", "Protect those feet!"),
    "item_note_2": item("item_note_2", "Note", "note_2.txt"),
    "item_note_3": item("item_note_3", "Note", "note_3.txt"),
    "item_coat": item("item_coat", "Coat", "An old fashioned grey coat made out of luxurious feeling wool thread. You "
                                           "really enjoy the style and it seems very comfortable to be fair."),
    "item_lighter": item("item_lighter","Lighter","This may be useful."),
    "item_lipstick": item("item_lipstick","lipstick","An elegant looking lipstick in black and silver. There is a "
                                                     "word “Hannah” engraved on the silver handle part."),
    "item_shirt": item("item_shirt","Shirt","A white satin shirt with a breast pocket. You wonder how the shirt "
                                            "remained so sparklingly white considering the surroundings it has been "
                                            "around."),
    "item_trousers": item("item_trousers","Trousers","A pair of smooth, black pants that taper from the knee "
                                                     "downwards. The pants haven’t been washed in a while but they "
                                                     "aren’t dirty or stink. Just worn out."),
    "item_cigarettes": item("item_cigarettes","Cigarettes","Only got a few left."),
    "item_pink_slip": item("item_pink_slip","Pink slip","A notice of dismissal from work."),
    "item_work_ID": item("item_work_ID","Work ID","Won't be needing this anymore."),
    "item_vial": item("item_vial","Empty vial","A vial with a couple drops of black liquid  remaining in the bottom"),
    "item_bar_card": item("item_bar_card","Bar card","The Shining Star. Private bar located on floor 5. Show card upon entry."),
    "item_scrap1": item("item_scrap1","Scrap paper","Piece 1 out of 4"),
    "item_scrap2": item("item_scrap2","Scrap paper","Piece 2 out of 4"),
    "item_scrap3": item("item_scrap3","Scrap paper","Piece 3 out of 4"),
    "item_scrap4": item("item_scrap4","Scrap paper","Piece 4 out of 4"),
    "item_finished_note": item("item_finished_note","Finished note","note_6.txt"),
    "item_note_cipher" : item("item_note_cipher","Note", "note_4.txt"),
    "item_note_cipher_key" : item("item_note_cipher_key","Note", "note_5.txt"),
    "item_master_keycard": item("item_master_keycard","Personal Keycard","Allows you to travel to ground floor, and top floor.")

}
