import io
import os

import pygame

filename = "text/logo.txt"

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

pygame.mixer.init()
pygame.mixer.music.load("sounds/startmenu.wav")
clear()

def startScreen():
    pygame.mixer.music.play(-1)
    ready=False
    while not ready:
        options=start_menu()
        ready=options[0]
        debug=options[1]
    pygame.mixer.music.stop()
    return "debug" if debug else "player"


def show_instructions():
    print("--- HOW TO PLAY ---")
    print('')
    print("- Set the scene:")
    print("The year is 2040")
    print("Some nights are crazy, a bit too crazy...")
    print("Last night was one of those 'too crazy' ones.")
    print("You wake up in a room, alone, in a studio apartment block.")
    print("Your aim is to find your belongings and clothes, piece together your memory from last night,")
    print("and escape the building")
    print('')
    print("- Navigation & Gameplay:")
    print("You will be given lists of commands that you can use to navigate your way round the building, ")
    print("pick up your belongings, and gain information.")
    print("Use simple commands like 'GO 1' to enter Room 1, or TAKE FORK to pickup a fork (hint)")
    print("You can also view your inventory, here you can see what you've picked up throughout the day,")
    print("and can also read any notes you may have acquired.")
    print("You can type 'help' to bring up a help menu")
    print('')
    print("That's it.")
    print("Good luck.")
    print('')
    print("--FOR BEST RESULTS USE FULL SCREEN--")
    print('')


def start_menu():
    ready=False
    debugMode=False
    print("")
    with io.open(filename, "r", encoding="utf8") as f:
        print("".join(f.readlines()))
    print("")

    # uncomment at release
    # inp = input("Type START if you think you're ready.\n>> ")

    # remove at release

    show_instructions()

    inp = input("Type START if you think you're ready.\n>> ").lower()

    if inp == "start":
        ready = True
    elif inp == "debug":
        debugMode = True
        ready = True
    return [ready, debugMode]


if __name__ == '__main__':
    startScreen()