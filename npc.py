import sys
from time import sleep

import pygame

pygame.mixer.init()

def type_print(val, time):
    for x in val:
        
        print(x, end='')
        sys.stdout.flush()
        sleep(time)
        
class npc:
    def __init__(self, id, name, text, speech = None, will_take = None, items = None): #willTake is a dictionary where the key is a item the npc will accept and the value is what the npc will say as a result
        self.id=id
        self.name=name
        self.text=text
        if speech:
            self.speech=pygame.mixer.Sound("NPCdialog\\"+speech)
        else:
            self.speech=None
        self.will_take = will_take
        self.items = items

    def speak(self,textFile=None):
        if not textFile:
            textFile = self.text
        if self.speech:
            pygame.mixer.Sound.play(self.speech)
        with open(textFile,"r") as file:
            for line in file.readlines():
                type_print(line,0.06)
        print("\n")

    def take_item(self,item):
        if item in self.will_take:
            self.speak(self.will_take[item])
        else:
            type_print(f"I dont want {item}.",0.1)


npcs = {
        "hannah": npc("hannah","Hannah","NPCdialog/hannah.txt", will_take={"item_lipstick":"NPCdialog/lipstick.txt"}, items=["item_coat", "item_wallet"]),
        "peter": npc("peter","Peter","NPCdialog/peter.txt",items=["item_trousers", "item_work_ID"]),
        "magpie": npc("magpie","Magpie","NPCdialog/magpie.txt", will_take={"item_vial":"NPCdialog/vial.txt"})
        }
