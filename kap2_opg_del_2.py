#---------Importeringer-----------|
from fractions import Fraction
from hashlib import new
from multiprocessing.dummy import Array
from operator import index
import os                        
import math
import numpy 
def clear():                     
    os.system('cls')    
#---------------------------------|

# Oppgaver Kap 2. Del 2
# Tema: input!
# Oppgave 16.
# Lag et program som tar navnet ditt som input og skriver ut "Hei, <navnet ditt>"

def navn():
    clear() # Jeg syntes dette blir penere å inkludere denne funksjonaliteten i små program.
    n = input("Hei, hva er navnet ditt?\n")
    print("Hei,",n)


# Oppgave 17.
# Lag et program som tar antall år som input og konverterer det til sekunder. Du kan se bort ifra skuddår.

def år():
    clear()
    ant_år = float(input("Hvor mange år skal konverteres til sekunder?\n"))
    a = (ant_år * 365 * 24 * 60 * 60)
    print(a)

#Oppgave 18.
# Lag et program som tar to tall "a" og "b" som input. Tallet "a" skal så deles på b. Resultatet skal
# skrives ut på dette formatet: a/b = <antalll ganger "a" går opp i "b"> + <rest>

def aogb():
    clear()
    
    tall_1 = float(input("Hva skal tall \"a\" være?\n"))
    tall_2 = float(input("Hva skal tall \"b\" være?\n"))
    
    calc = float(tall_1/tall_2)
    calc_2 = float(tall_1%tall_2)
    if calc % 2 == 0: #dersom det ikke er noe rest-verdi 
        print(tall_1,"/", tall_2,"=", calc)
    else:
        print(tall_1,"/", tall_2,"=", calc, "+",calc_2)

# Oppgave 19 utgår (denne er den samme oppgaven som oppgave 7)

# Oppgave 20.
# Lag et program som regner ut arealet og omkretsen av et parallellogram.

def para():
    clear()
    inn = input("Hei, vil du regne ut arealet eller omkretsen?\na: Areal\no: Omkrets\n")
    if inn == "a": #areal
        clear()
    #bruker fører input
        a = float(input("Hva er lengden på grunnlinjen?\n"))
        b = float(input("Hva er høyden?\n"))
    #utregning av areal
        areal = a * b
        print("Omkretsen på ditt parallellogram er:", areal)
    elif inn == "o": #omkrets
        clear()
        #utregning av omkrets
        a = float(input("\nHva er lengden på side \"a\"?\n"))
        b = float(input("\nHva er lengden på side \"b\"?\n"))    
        omkrets = a * 2 + b * 2
        print("Omkretsen på ditt parallellogram er:",omkrets)
    else: 
        para()

# Oppgave 21
# Lag et program som regner ut overflaten og volumet av en kule.
def kule():
    clear()
    inn = input("Hei, vil du regne ut Overflaten eller Volumet av kulen?\no: Overflaten\nv: Volumet\n")
    if inn == "o":
        #bruker må gi input
        clear()
        r = float(input("Hva er radiusen på kulen?\n"))
        calc = round((4 * math.pi * r**2),2) #Utregning av overflate for en kule
        print("Overflaten på kulen med radius:", r, "=",calc)
    
    elif inn == "v":
        clear()
        #bruker må gi input
        r = float(input("Hva er radiusen på kulen?\n"))
        calc_2 = 4.0/3.0*math.pi*r**3  # Her har man gjort om formelen, slik at det ikke kommer float og int på samme brøkstrek - tror jeg. Hadde jeg fulgt en formel som vist her
                                       # https://bit.ly/3omDfb6 ville det ikke blitt riktig - jeg fikk error og virker som dette har med at "pi" ikke kan stå
                                       # som en del av brøken. Derfor fulgte jeg https://bit.ly/3Bd7skz og fant en annen utregnings formelen isteden. Suksess!
        print("Volumet på kulen =", calc_2)
    else:
        kule()

# Oppgave 22:
# Lag et program som tar et grunntall "a" og en eksponent "n" som input og som skriver ut hva a^n blir. Bruk passende matematiske begreper når du lager variabler og skriver ut svaret.
def ekspo():
    clear()
    tall_1 = int(input("Hvilke tall skal være grunntall?\n"))
    tall_2 = int(input("Hvilke tall skal være eksponent?\n"))
    calc = tall_1**tall_2
    print(tall_1,"^",tall_2,"=", calc)

# Tema: Lister!
# Oppgave 23:
# Lag en liste med 8 partall, og en liste med 8 oddetall!
#
# Notater:
# " The range() function defaults to 0 as a starting value, 
# however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)"
#
# Lager listene her:
def lister_1():
    clear()
    list_1 = [] #array for partall
    list_2 = [] #array for oddetall
    for i in range(1,18): # Mellom tallene 1 og 18 er det 8 partall etter min beregning.
        if i%2 == 0:    # dersom i er et partall
            list_1.append(i) #legg til i partall
        elif i%2 == 1:  
            list_2.append(i) #legg til i oddetall
    print("\n",list_1,"\n",list_2) #Utskrift

# Prøv å addere de to listene. Hva skjer?
# svar: Det som skjer - eller, det jeg tror skjer er at listene, slik de sto plassert i forhold til "+" tegnet, så lages det en ny array med innhold fra begge listene.

def lister_2():
    clear()
    list_1 = [] 
    list_2 = [] 
    for i in range(1,18): 
        if i%2 == 0:   
            list_1.append(i) 
        elif i%2 == 1:  
            list_2.append(i)
    adding_it = (list_1 + list_2) #<------- Listene addert HER ^__^
    print(adding_it) 

# b) Kan du dele eller gange de to listene med hverandre?
# Tja, let's find out?
# Første feilmelding fra koden under er: "can't multiply sequence by non-int of type 'list'"
# Men skal søke om andre muligheter for å få dette til..
# Finner dette: https://www.geeksforgeeks.org/numpy-multiply-in-python/

def lister_3():
    clear()
    list_1 = [] 
    list_2 = [] 
    for i in range(1,18): 
        if i%2 == 0:   
            list_1.append(i) 
        elif i%2 == 1:  
            list_2.append(i)
    multi_it = list_1 * list_2 #<------- Listene multiplisert HER
    print(multi_it) 
#lister_3()

#Sånn. Det er vist flere måter å gjøre dette på. Intuitivt valgte jeg denne metoden (arr_1[0] / arr_2[0], arr_1[1] / arr_2[1] osv...):
# Multiplikasjon av 2 arrays:
def multi_arr():
    arr_1 = numpy.array([1,2,3,4,5])
    arr_2 = numpy.array([6,7,8,9,10])
    ut = numpy.multiply(arr_1, arr_2)
    print(ut)
#multi_arr()

# Divisjon av 2 arrays: # formateringen er litt rar, men funker å dele hvertfall. ^__^
def dividian_arr():
    arr_1 = numpy.array([100,200,300,400,500])
    arr_2 = numpy.array([15,20,30,45,100])
    ut = numpy.divide(arr_1,arr_2)
    print(ut)
#dividian_arr()

# Jeg innså at jeg skulle bruke samme lister fra første oppgave, ble litt leken og lagde nye lister jeg da.
# Her er oppgaven(e) med bruk av samme liste som i oppgave a og b:

def lister_4():
   l = numpy.array([2,4,6,8,10,12,14,16])
   j = numpy.array([1,3,5,7,9,11,13,15])
   print(l*j) #multipliserer "array l" og "array j"
#lister_4()

def lister_5():
   l = numpy.array([2,4,6,8,10,12,14,16])
   j = numpy.array([1,3,5,7,9,11,13,15])
   print(l/j) #divisjon av "array l" og "array j". Utskriften er litt rar, men dette har med antall desimaler å gjøre. kan ikke bruke round() virker det til.
#lister_5()

# c)
# skriv ut det første, det siste og de to midterste tallene fra en av listene.
def fancy_1():
    clear()
    list_1 = [] #array for partall
    list_2 = [] #array for oddetall
    for i in range(1,18): 
        if i%2 == 0:    
            list_1.append(i) 
        elif i%2 == 1:  
            list_2.append(i) 
    print(list_1)
    print("\nFørste:",list_1[0],"\nSiste:",list_1[-1],"\nNr.4:",list_1[3],"\nNr.5:",list_1[4]) # Nr. 4 og Nr.5 fungerer bare å finne slik, når jeg vet størrelsen på lista.
#fancy_1()

# d)
# Legg til et element i begge listene, og slett det tredje elementet i hver av dem.
def fancy_2():
    clear()
    list_1 = [] #array for partall
    list_2 = [] #array for oddetall
    for i in range(1,18): 
        if i%2 == 0:    
            list_1.append(i) 
        elif i%2 == 1:  
            list_2.append(i) 
    print("Opprinnelig:", list_1) # utskrift før jeg legger til flere liste-elementer.
    
    list_1.append(88) #legger til 88 i partalls-lista
    list_2.append(1427) # legger til 1427 i oddetalls-lista
    del list_1[2] # Fjerner det tredje elementet i partalls-lista
    del list_2[2] # Fjerner det tredje elementet i oddetalls-lista
    print("Endret:")
    print(list_1, list_2)
#fancy_2()

# Oppgave 24:
# Lag to ulike lister med favorittbøker, TV-serier, fotballspillere eller lignende. Listene bør ha minst fem elementer hver.
# 
# a) Slå sammen listene.
# b) Slett det første og det tredje elementet i den sammenslåtte lista.
# c) Finn ut hvilke indeks ett av elementene har. 
# d) Lag en ny liste av element 3-6
# e) Reverser lista.
#
# Jeg har valgt dette som innhold i listene:
# Snus varemerker:
# General, Skruf, The Lab, Thunder, Omni, Granit, Islay, Lundgrens
#
# Varemerker av fritids kniver: 
# Strømeng, Øyo, Brusletto, Helle, Mora, Fjellreven
snus_arr = ["General","Skruf","The Lab","Thunder","Omni","Granit","Islay","Lundgrens"]
kniv_arr = ["Strømeng","Øyo","Brusletto","Helle","Mora","Fjellreven"]

# a) Slå sammen listene.
def add_dem(a,b):
    clear()
    a = snus_arr + kniv_arr
    return a
#print(add_dem(snus_arr,kniv_arr)) 

# b) Slett det første og det tredje elementet i den sammenslåtte lista.
def edit_dem(a,b): 
    merge_1 = snus_arr + kniv_arr
    del merge_1[0]
    del merge_1[2]
    return merge_1
#print("Orginal:",add_dem(snus_arr,kniv_arr)) #utskrift
#print("Endret:",edit_dem(snus_arr,kniv_arr)) #utskrift

# c) Finn ut hvilke indeks ett av elementene har.
# Notat: https://www.programiz.com/python-programming/methods/list/index
def find_it():
    merged_lists = (snus_arr + kniv_arr)
    inx = merged_lists.index('Mora')
    print(inx)
#find_it()

# d) Lag en ny liste av element 3-6
def do_it():
    new_merge = []
    merged_lists = (snus_arr + kniv_arr)
    new_merge.append(merged_lists[2]) # forsøkte å finne andre måter å gjøre dette på. Men litt CBA, har kodet i 7 timer i strekk nå.
    new_merge.append(merged_lists[3]) # Løsningene blir litt der-etter. Yawn!
    new_merge.append(merged_lists[4])
    new_merge.append(merged_lists[5])
    print(new_merge)
#do_it()

def rew_it():
    new_merge = []
    merged_lists = (snus_arr + kniv_arr)
    merged_lists.reverse() #Reverserer den sammenslåtte lista.
    new_merge.append(merged_lists)
    print(new_merge)
rew_it()

# Se, en gresshoppe!
#   //_____ __       
#   @ )====// .\___
#   \#\_\__(_/_\\_/
#     / /       \\
