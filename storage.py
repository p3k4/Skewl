import os
#Skriv et sett med instruksjoner som du kan bruke til å komme deg igjennom dagligvarebutikken.
kjøleskap = ["milk", "bread", "fish", "beer"]
handleliste = []
butikk = ["milk","butter","bread","liver","jam","ham","chees","beer", "juice", "fish","meat","salad"]

## Funksjoner
#Program intro.
def run():
    clear()
    print('Hi! I am SuperShop, your personal shopping application!')
    print('--Version 1.0\n')

def lag_liste():
    x = 1
    while x == 1:
        clear()
        print_list()
        com_1()
        vare = str(input("Please write a product you wish to add to your shopping-list:\n").lower())
        handleliste.append(vare)
        if vare == "x":
            fjern_liste()
            clear()
            print_list()
        elif vare == "b":
            x = 0
            fjern_liste()
            clear()
            dostuff()
        elif vare == "z":
            rm_last()
            print_list()

def print_list():
    print("Shoppinglist:", handleliste, "\n")

#def rm_last(): MEN @ WORK!!

def clear():
    os.system('cls||clear')

def fjern_liste():
   handleliste.clear()

def com_1():
    print("Additional commands:\nx: Empty shopping-list.\nb: Go back\nz:Remove last item.\n")

#starter programmet, sender bruker til "start og program venter på videre kommando"
def dostuff():
    run()
    print("Avaliable commands:\ns: Shop \nc: Create your shopping-list \n")
    kom = input("Please type your command:\n".lower())
    #kjører programmet fra begynnelsen om input er tom
    if kom =="":
        clear()
        dostuff()    
    elif kom == "s":
        clear()                         #fjernet innholdet i terminalen. Samme som en "clear()" funksjon
        #shop()                         #funksjon for å shoppe
    elif kom == "c":
        clear()                         #fjernet innholdet i terminalen. Samme som en "clear()" funksjon
        lag_liste()                     #dersom ingen av de tilgjengelige kommandoene blir kjørt, starter programmet fra begynnelsen
    else:
        clear()                         #fjernet innholdet i terminalen. Samme som en "clear()" funksjon
        run()
        dostuff()                       #kjører programmet fra begynnelsen.
dostuff()