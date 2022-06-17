#SuperShopper. 1.0.6
from distutils import cmd
import os
from turtle import clear

def art(): #Shopping-art. l0l
    print("    .'o O'-._")
    print("   / O o_.-`|")
    print("  /O_.-'  O |")
    print(" | o   o .-`")
    print(" |o O_.-'")
    print(" '--` ")
    print("SuperShopper --Version 1.0.6\n")

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
# Could "users bagpack" be a thing? I'm still gonna add a fridge, cause I can and most seniable ppl store their groceries there.
fridge = ["melk","brød","smør","ost","syltetøy","ost"]
# Array for "new shopping-list".
handleliste = []
#Array for products supported in the system. Both handleliste, fridge and store.
produkter = ["melk","brød","smør","øl","syltetøy","ost","skinke","brus","brunost","muggost"]

def do_a():
    #Fresh window - clear screen. loading art and showing "handleliste"
    clear() #sorting out bugs
    art()   #sorting out bugs
    print_list()
    #User input - table of available commands
    kom = str(input("1: Add items to the list.\n2: Delete all items.\n3: Delete last item added to the list.\n4: Delete item by name.\nb: go back..\n"))
    if kom == "1": #Create New Shopping-list
        clear()
        art()
        populate_list() # Sending user to "Add products/items to the shopping-list, specifically"
    elif kom == "2":
        handleliste.clear() ##sorting out bugs
        clear() #sorting out bugs
        do_a()  #sorting out bugs
    elif kom == "3":
        del handleliste[-1]
        clear() #sorting out bugs
        do_a()  #sorting out bugs
    elif kom == "b":
        handleliste.clear() #sorting out bugs
        clear()     #sorting out bugs
        default()   #sending user to "default-program-mode"
    else:
        clear() #sorting out bugs
        do_a()  #Fresh window - clear screen. loading art and showing "handleliste"

def populate_list(): #function to populate handleliste
    clear()
    art()
    #print("In store: ",*produkter, ".") Legge til å vise produkter, kjølesap etc?
    #print("In my fridge: ", str(fridge), "\n")
    #print("Shopping-list: ", str(handleliste))
    x = 1
    while x == 1:
        vare = str(input("Please write a product you wish to add to your shopping-list:\n").lower())
        if vare not in produkter:
            clear() #sorting out bugs
            x = 0   #stops the while-true loop
            do_a()  #Fresh window - clear screen. loading art and showing "handleliste"
        elif vare == "b":   #sorting out bugs
            clear()         #sorting out bugs
            x = 0           #stops the while-true loop
            do_a()          #Fresh window - clear screen. loading art and showing "handleliste"
        else:
            handleliste.append(vare)    #adds item/user-input to the new Shopping-list
            x = 0           #stops the while-true loop
            do_a()          #Fresh window - clear screen. loading art and showing "handleliste"
def end():                  
    print("Buy-bye!")       #this is missing from do_a() "page". Work to do. Work-work!
    exit()                  

def print_list(): # Mulighet for å formatere handlelisten som vises.. mange ulike måter å formatere på, har ikke bestemt hvilke ennå.
    print("Shoppinglist:", handleliste, "\n")

def clear():                #Funksjon som fjerner alt innhold i terminalen.
    os.system('cls||clear')

def output(list):           # Mulighet for å formatere handlelisten som vises.. mange ulike måter å formatere på, har ikke bestemt hvilke ennå.
   print(' '.join(map(str, list)))

commands_1 = { #Commands table 1
    "b": default,   #done
    "end": end,     #done
    "1": do_a       #done
#    "3": do_c      #Mangler
#    "4": do_d      #Mangler
}

while True:     #kjører igang programmet.
    commands_1.get(cmd, default)()
    cmd = input("").lower() #styrer command table 1
