#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from colorama import Fore as colour_directory
import os
import time
import sys
import keyboard

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

try :
    OpenFile = open(os.getcwd()+"\\Data\\RefFile","r")
    OpenFile.close()
except FileNotFoundError :
    os.mkdir(os.getcwd()+"\\Data")
    OpenFile = open(os.getcwd()+"\\Data\\RefFile","w")
    OpenFile.write("Reference point for file creation.")
    OpenFile.close()
    OpenFile = open(os.getcwd()+"\\Data\\Save1","w")
    OpenFile.close()
    OpenFile = open(os.getcwd()+"\\Data\\Save2","w")
    OpenFile.close()
    OpenFile = open(os.getcwd()+"\\Data\\Save3","w")
    OpenFile.close()
    OpenFile = open(os.getcwd()+"\\Data\\Save4","w")
    OpenFile.close()
    OpenFile = open(os.getcwd()+"\\Data\\Save5","w")
    OpenFile.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

player_name = ""
player_class = ""

STR = 0
DEX = 0
CON = 0
INT = 0
WIS = 0
CHA = 0

saveFile = 0
saves = {1:False,2:False,3:False,4:False,5:False}

input_text_colour = colour_directory.LIGHTBLACK_EX
positive_colour = colour_directory.GREEN
negative_colour = colour_directory.RED
neutral_colour = colour_directory.BLUE

classes = {"Wizard":"Placeholder",
           "Rogue":"Placeholder",
           "Monk":"Placeholder",
           "Artificer":"Placeholder",
           "Paladin":"Placeholder",
           "Priest":"Placeholder",
           "Bard":"Placeholder",}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def SelectMenu(Options, Returns, Prefix = "") :
    selected = 0
    loop = True

    while loop :
        Clear()
        print(Prefix)

        for c in Options :
            if c == Options[selected] :
                Col = colour_directory.BLUE
            else :
                Col = colour_directory.LIGHTBLACK_EX
            print(Col+c)
        print(colour_directory.MAGENTA+"\n"+Options[selected])

        key = keyboard.read_key()
        while keyboard.is_pressed(key) :
            keyboard.read_event()
        
        if key != "" :
            if key == "down" :
                if selected+1 < len(Options) :
                    selected += 1
            elif key == "up" :
                if selected-1 >= 0 :
                    selected -= 1
            elif key == "enter" :
                Clear()
                print(Prefix)
                return Returns[selected]

def Input(prompt="", existing = None):

    Clear()
    user_input = []
    EditingCharacter = 0
    EditingCharacterModifier = 0
    EditingCharacter = len(user_input)+EditingCharacterModifier-1

    if existing != None :
        for c in existing :
            user_input.append(c)
        user_input.insert(len(user_input),colour_directory.MAGENTA+"_")
        print(prompt+"".join(user_input))
    else :
        user_input.insert(EditingCharacter,colour_directory.MAGENTA+"_")
        print(prompt, end='', flush=True)

    while True:
        EditingCharacter = len(user_input)+EditingCharacterModifier-1
        event = keyboard.read_event()

        user_input.remove(colour_directory.MAGENTA+"_")
        user_input.insert(EditingCharacter,colour_directory.MAGENTA+"_")

        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == "left" and EditingCharacter + EditingCharacterModifier - 1 >= 0-(len(user_input)-1) :
                EditingCharacterModifier -= 1
                EditingCharacter = len(user_input)+EditingCharacterModifier-1
                user_input.remove(colour_directory.MAGENTA+"_")
                user_input.insert(EditingCharacter,colour_directory.MAGENTA+"_")
                Clear()
                print(prompt+"".join(user_input))

            elif key == "right" and EditingCharacter + EditingCharacterModifier + 1 <= len(user_input)-1 :
                EditingCharacterModifier += 1
                EditingCharacter = len(user_input)+EditingCharacterModifier-1
                user_input.remove(colour_directory.MAGENTA+"_")
                user_input.insert(EditingCharacter,colour_directory.MAGENTA+"_")
                Clear()
                print(prompt+"".join(user_input))

            elif key == 'enter':
                if (not keyboard.is_pressed("shift")) and (not keyboard.is_pressed("right shift")) :
                    print()
                    break
                else :
                    user_input.insert(EditingCharacter,"\n")
                    Clear()
                    print(prompt+"".join(user_input))

            elif key == 'backspace':
                if EditingCharacter > 0 :
                    user_input.pop(EditingCharacter-1)
                    Clear()
                    print(prompt+"".join(user_input))

            elif len(key) == 1:
                user_input.insert(EditingCharacter,key)
                Clear()
                print(prompt+"".join(user_input))
            elif key == "space" :
                user_input.insert(EditingCharacter," ")
                Clear()
                print(prompt+"".join(user_input))

    if colour_directory.MAGENTA+"_" in user_input :
        user_input.remove(colour_directory.MAGENTA+"_")
    return ''.join(user_input)

def Clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

