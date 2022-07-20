# tall, variabler, lister av tall og av andre verdier.

# variabler eks. 1
# jeg slenger også med datatyper som er veldig vanlige å forholde seg til.

from turtle import clear

#a = 10 # int (haltall)
#b = 3.14 # float (desimaltall)
#c = "Summer er" # string (tekst)

#print(c, a + b)

#underveisoppgave 2.1: Flyttall og desimaltall. Hvorfor blir dette feil?
#print((0.1 + 0.2) * 3)

# Er det noe med regnerekkefølen? SVAR: Nei.
# Rekkefølgen er:
# Parenteser
# Potenser og røtter
# Divisjon og multiplikasjon
# Addisjon og subtraksjon

# Python tar med en hel drøss desimaler - kan det være dette de mener er feil?
# jeg legger til round() for å avrunde til nærmeste heltall:
# print(round((0.1 + 0.2) * 3))

# standardform/potenser (eksponent og grunntall)
# altså: 1.4 * 10^12
# skrives i Python slik, aEb (a er grunntallet og b er eksponenten):
#d = 1.4 * 10E12
#print(d)

# OBS!
# Det er verdt å merke seg, at Python (som er så lur.. hihi) tolker alle tall som oppgis på standardform som et flyttall (float)
# også hvis tallet i utgangspunktet er et heltall!
# Kan likevel "caste" for å tvinge frem en annen datatype.
#e = int (10E0)
#print(e)

# Variabler
# * Kan ikke begynne med et tall, eller inneholde et punktum, komma eller binnestrek (understrek funker derimot fint-fint)
# Opprettelse av variabler kan se slik ut:
#x = 5
#y = 2
#z = x + y
#print(z)

# = er ikke å tolke på samme måte som en matematisk-likning. Viktig å huske på.
#i = 5
#j = i + 10

# = betyr "tilordning".
# == betyr "nøyaktig verdi"
# === betyr "samme plass i minne"

# Hvilke utfordringer og muligheter gir det at bruken av likhetstegnet er forskjellig i matematikk og programmering?

# Utfordringer: Noobs need 2 get gud
# Muligheter: Verdensherredømme.

# Casting
#tall = 3 # et heltall (int)
#tekst = str(tall)
#print(tall) # int verdi
#print(tekst) # stringverdi

#fancy stuff 4 nørds:
#m = 4.0
#v = 2.0
#k_e = 0.5*m*v**2 #akkurat.. "**" betyr potens!
#print("Den kinetiske energien er:", k_e, "joule") 

#string
# "" brukes for å understreke teksten mht. skriveregler. F.eks. ironi
# ' ' brukes for streng-verdi
# string forkortes til "str"
#beskjed1 = 'Jeg er "kulere" enn deg'
#beskjed2= 'den er grei!'
#print (beskjed1, "\n", beskjed2)

# Boolske variabler: True / false
# print()
#a_1 = 1
#b_1 = 3 
#c_1 = 4

#print(a_1 == b_1) # false
#print(b_1 < a_1) # flase
#print(b_1 > a_1 and b_1 > c_1) # false
#print(b_1 >= a_1) # true
#print(b != a_1) # true
#print(b_1 > a_1 or b_1 > c_1) # true

#list comprehension <--- Innspill fra Ivar (hyggelig og belest utvikler fra Stavanger)
#liste = ["ola","Per","Kari"]
#for i in liste:
#    print(i)

# print([(x + "smith") for x in liste if len(x) > 3]) 

# Aritmetikk / Operatorer
# Heltall     |  44
# Desimaltall |  3.1415
# Stren/tekst | "Hade!"
# Boolean     | True

# addisjon           | +
# Substraksjon       | -
# Divisjon           | /
# Multiplikasjon     | *
# Potens             | **
# Heltalls-divisjon  | //    <-- I en heltallsdivisjon runder vi ned til det nærmeste heltallet divisjonen går opp i- 26 // 5 
# Modulus            | %     <-- I en modolus gir oss rest-verdien etter en heltallsdivisjon. 26 % 5 = 1 

# underveisopopgave 2.4:
# Hvordan kan du teste om et tall er partall eller oddetall ved hjelp av modulusoperatoren? Prøv deg frem!
# --------------------------------------------------------------------------------------------------------------------------
#tall = int(input("Hvilke tall skal sjekkes?\n")) # Ber bruker om tall som skal sjekkes om er partall eller oddetall
#if tall % 2 == 0: #dersom "tall" gitt av brukeren gir 0 i rest etter heltallsdivisjon på 2 (partall gir 0 i rest)
#    print(tall, "<-- Tallet er partall") # skrives dette
#else: # eller
#    print(tall, "<-- Talet er oddetall") #dersom "tall" gir en restverdi (er oddtall) skrives dette
# ---------------------------------------------------------------------------------------------------------------------------
# Repitisjon - dette må kunnes godt, spesielt når vi vet at alle utregninger blir satt opp linært på en datamaskin/et program: 

# Regne-rekkefølge
# Parenteser
# Potenser og røtter
# Divisjon og multiplikasjon
# Addisjon og subtraksjon

# 2.8 liuste
# tom_liste = []
# liste_som_har_innhold = ["EN","TO","TRE"]
# rotete_liste = ["Navn",1,2] <-- Dette er mulig, men ikke noe vi ønsker. Det blir mye å ta hensyn til med rotete lister, ha derfor en liste for hver enkelt datatype.

# "number - 1" konseptet illustrert:
# Python-lister er indeksert fra 0 og siste element får indeks (n - 1). Altså, en liste på 5 starter listen på 0, og siste posisjon er 4.

#---------------------------------
#liste_a = [1,2,3,4,5]
#for i in range(0,len(liste_a)):
#    print(i)
#---------------------------------

#tall = [1,3,5,7]
#print(tall[0]) # Gir utskrift "1"
#print(tall[3]) # Gir utskrift "5"

#summen = tall[1] + tall[2] # Legger sammen (addisjon) to av liste-elemetenes verdi
#print(summen) # Skriver ut denne verdien

#verdier = [1,2,3,4] 
#verdier.append(5) #Her er lista nå ineksert til 
#verdier.remove(2) # Fjerner første forekomsten av denne gitte verdien (2) i lista.
#print(len(verdier)) # len() funksjonen returnerer antall elementer i lista, og IKKE indekseringen!

# Spørsmål: Hvor lang er lista nå?
# Svar:
# Det finnes minst to svar på dette; 
# Antall elementer i lista = 4
# Men indekseringen er fra 0 til 4, altså 5. 
# Hva er indeks for verdien 3?
# Svar: 1
# Kan sjekkes med å kjøre denne linjen med kode:
# print(verdier[1])

# Underveisoppgave:
# Lag to lister, hver liste skal innholde 5 tall. Prøv ut føløgende operasjoner:
liste_a = [0,8,13,24,28]
liste_b = [11,3,42,54,45]

# 1: Slette det siste elementet i den ene lista.
# 2: Legge til et tall i den andre lista.
# 3: Lage en ny variabel der du adderer listene. Dette blir en ny liste.
# 4: Skriv ut de tre listene. Hva har skjedd?

# liste_a.remove(liste_a[4]) <-- Europris-løsning, men la oss si at vi ikke vet lengden på lista 
# print(liste_a)

lengden_på_lista = len(liste_a) #returnerer verdien av antall elementer i liste_a
#print(lengden_på_lista)
liste_a.remove(liste_a[lengden_på_lista - 1]) # Fjerner siste element i lista
print(liste_a[-1]) # some_array[-1] vil alltid peke til siste list-element. Vi kan skrive [-1], [-2], [-3], [-4] for å peke baklengs i lista! Fancy stuff!
 
