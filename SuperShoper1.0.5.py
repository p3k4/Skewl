#SuperShopper. 1.0.5
from distutils import cmd
import os
from turtle import clear

def art():
    print("    .'o O'-._")
    print("   / O o_.-`|")
    print("  /O_.-'  O |")
    print(" | o   o .-`")
    print(" |o O_.-'")
    print(" '--` ")
    print("SuperShopper --Version 1.0.5\n")

def default():
    os.system('cls||clear')
    art()
    print("1: Create new Shopping-list!\n2: See what the shop has in store just now!\n3: Look at stored items in your fridge..\n4: Look at stored items in your bagpack..\n\nOr type \'end' to exit")

# Scenario:end
# User runs "c" command
# Creates an empty one-dimentional array "handleliste", 
# Tells user: Please write a product you wish to add to your shopping-list \n
# User-inputs items.
# Updates the array.

# Avaliable commands:
# b: Sends user to the intro-screen.
# x: Removes all liste items in the Shopping-list.
# z: Removes the last element in the list. 
#
# User goes shopping scenario:
# If the store has the item in stock - it will be added to your trolley. \n
# If the item is not in the store, it will not be added. \n
#
# Users bagpack (to bring products home)
#
handleliste = []
produkter = ["melk","brød","smør","øl","syltetøy","ost","skinke","brus","brunost","muggost"]
fridge = ["melk","brød","smør","ost","syltetøy","ost"]

def do_a(): # command 1: Send user to "Create new Shopping-list"!
    clear()
    art()
    print_list()
    kom = str(input("1: Add items to the list.\n2: Delete all items.\n3: Delete last item added to the list.\n4: Delete item by name.\nb: go back..\n"))
    if kom == "1":
        clear()
        art()
        populate_list()
    elif kom == "2":
        handleliste.clear()
        clear()
        do_a()
    elif kom == "3":
        del handleliste[-1]
        clear()
        do_a()
    elif kom == "b":
        handleliste.clear()
        clear()
        default() 
    else:
        clear()
        do_a()

def populate_list():
    clear()
    art()
    #print("In store: ",*produkter, ".") Legge til å vise produkter, kjølesap etc?
    #print("In my fridge: ", str(fridge), "\n")
    #print("Shopping-list: ", str(handleliste))
    x = 1
    while x == 1:
        vare = str(input("Please write a product you wish to add to your shopping-list:\n").lower())
        if vare not in produkter:
            clear()
            x = 0
            do_a()        
        elif vare == "b":
            clear()
            x = 0
            do_a()
        else:
            handleliste.append(vare)
            x = 0
            do_a()
def end():
    print("Buy-bye!")
    exit()

def print_list(): # Mulighet for å formatere handlelisten som vises. 
    print("Shoppinglist:", handleliste, "\n")

def clear():
    os.system('cls||clear')

def output(list):
   print(' '.join(map(str, list)))

commands_1 = { #Commands
    "b": default,
    "end": end,
    "1": do_a
#    "3": do_c
#    "4": do_d
}

while True:
    commands_1.get(cmd, default)()
    cmd = input("").lower()
