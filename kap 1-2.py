# tall, variabler, lister av tall og av andre verdier.

# variabler eks. 1
# jeg slenger også med datatyper som er veldig vanlige å forholde seg til.

from turtle import clear

# a = 10 # int (haltall)
# b = 3.14 # float (desimaltall)
# c = "Summer er" # string (tekst)

# print(c, a + b)

# underveisoppgave 2.1: Flyttall og desimaltall. Hvorfor blir dette feil?
# print((0.1 + 0.2) * 3)

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
# d = 1.4 * 10E12
# print(d)

# OBS!
# Det er verdt å merke seg, at Python (som er så lur.. hihi) tolker alle tall som oppgis på standardform som et flyttall (float)
# også hvis tallet i utgangspunktet er et heltall!
# Kan likevel "caste" for å tvinge frem en annen datatype.
# e = int (10E0)
# print(e)

# Variabler
# * Kan ikke begynne med et tall, eller inneholde et punktum, komma eller binnestrek (understrek funker derimot fint-fint)
# Opprettelse av variabler kan se slik ut:
# x = 5
# y = 2
# z = x + y
# print(z)

# = er ikke å tolke på samme måte som en matematisk-likning. Viktig å huske på.
# i = 5
# j = i + 10

# = betyr "tilordning".
# == betyr "nøyaktig verdi"
# === betyr "samme plass i minne"

# Hvilke utfordringer og muligheter gir det at bruken av likhetstegnet er forskjellig i matematikk og programmering?

# Utfordringer: Noobs need 2 get gud
# Muligheter: Verdensherredømme.

# Casting
# tall = 3 # et heltall (int)
# tekst = str(tall)
# print(tall) # int verdi
# print(tekst) # stringverdi

# fancy stuff 4 nørds:
# m = 4.0
# v = 2.0
# k_e = 0.5*m*v**2 #akkurat.. "**" betyr potens!
# print("Den kinetiske energien er:", k_e, "joule") 

# string
# "" brukes for å understreke teksten mht. skriveregler. F.eks. ironi
# ' ' brukes for streng-verdi
# string forkortes til "str"
# beskjed1 = 'Jeg er "kulere" enn deg'
# beskjed2= 'den er grei!'
# print (beskjed1, "\n", beskjed2)

# Boolske variabler: True / false
# print()
# a_1 = 1
# b_1 = 3 
# c_1 = 4

# print(a_1 == b_1) # false
# print(b_1 < a_1) # flase
# print(b_1 > a_1 and b_1 > c_1) # false
# print(b_1 >= a_1) # true
# print(b != a_1) # true
# print(b_1 > a_1 or b_1 > c_1) # true

# list comprehension <--- Innspill fra Ivar (hyggelig og belest utvikler fra Stavanger)
# liste = ["ola","Per","Kari"]
# for i in liste:
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
#---------------------------------------------------------------------------------------------------------------------------
# tall = int(input("Hvilke tall skal sjekkes?\n")) # Ber bruker om tall som skal sjekkes om er partall eller oddetall
# if tall % 2 == 0: #dersom "tall" gitt av brukeren gir 0 i rest etter heltallsdivisjon på 2 (partall gir 0 i rest)
#    print(tall, "<-- Tallet er partall") # skrives dette
# else: # eller
#    print(tall, "<-- Talet er oddetall") #dersom "tall" gir en restverdi (er oddtall) skrives dette
#----------------------------------------------------------------------------------------------------------------------------
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
# liste_a = [1,2,3,4,5]
# for i in range(0,len(liste_a)):
#    print(i)
#---------------------------------

# tall = [1,3,5,7]
# print(tall[0]) # Gir utskrift "1"
# print(tall[3]) # Gir utskrift "5"

# summen = tall[1] + tall[2] # Legger sammen (addisjon) to av liste-elemetenes verdi
# print(summen) # Skriver ut denne verdien

# verdier = [1,2,3,4] 
# verdier.append(5) #Her er lista nå ineksert til 
# verdier.remove(2) # Fjerner første forekomsten av denne gitte verdien (2) i lista.
# print(len(verdier)) # len() funksjonen returnerer antall elementer i lista, og IKKE indekseringen!

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
# liste_a = [0,8,13,24,28]
# liste_b = [11,3,42,54,45]

# 1: Slette det siste elementet i den ene lista.
# 2: Legge til et tall i den andre lista. Slett element nummer 2.
# 3: Lage en ny variabel der du adderer listene. Dette blir en ny liste.
# 4: Skriv ut de tre listene. Hva har skjedd?

# liste_a.remove(liste_a[4]) <-- Europris-løsning, men la oss si at vi ikke vet lengden på lista 
# print(liste_a)

# lengden_på_lista = len(liste_a) #returnerer verdien av antall elementer i liste_a
# print(lengden_på_lista)
# liste_a.remove(liste_a[lengden_på_lista - 1]) # Fjerner siste element i lista
# print(liste_a[-1]) # some_array[-1] vil alltid peke til siste list-element. Vi kan skrive [-1], [-2], [-3], [-4] for å peke baklengs i lista! Fancy stuff!

# Oppgave 2: Legg til et tall i den andre lista:
# liste_b.append(88) #Legger til et nytt element med verdien "88"
# print(liste_b[-1]) # Dette kan sjekkes med denne linjen av kode, og fungerer

# Oppgave 2: Slett element nr. 2
# liste_b.remove(liste_b[1]) #Fjerner elementet som står på plasseringen 1, altså element nr. 2
# print(liste_b) # Dette kan sjekkes med denne linjen av kode, og fungerer

# Oppgave 3:  Lage en ny variabel der du adderer listene. Dette blir en ny liste.
# ny_liste = liste_a + liste_b # Usikker, men tror det er slik de mener med å "multiplisere listene", altså ikke hvert enkelt av elementene.
# print(ny_liste)

# Oppgave 4:  Skriv ut de tre listene. Hva har skjedd?
# print(liste_a)
# print(liste_b)
# print(ny_liste)

# Først fjernet jeg siste element fra "liste_a", det var verdien "28". Dermed er lista slik: ["0,8,13,24"]
# Så la jeg til et nytt element med verdi "88" i den andre lista: liste_b. Dermed ble liste_b slik: ["11,3,42,54,45"]
# Så slettet jeg element nr.2 i "liste_b". liste_b ble dermed slik: ["11,42,54,45"] <-- Verdi "3" er fjernet
# "ny_liste" er bare listene "liste_a" og "liste_b" er "lagt sammen", og ikke hvor elementene er addert.

# Input fra bruker/kommandolinja:
#høyde = input("Hvor høy her du?\n")

# Vi kan "caste" for å formatere input som vi vil:
#høyde_desimal = float(høyde)
#print(høyde_desimal)

# Høde av mount-everest = 8849 moh.
# mount_e = 8849

# Hvor høyt befinner brukeren seg i moh.?
# b_moh = float(input("Hvor mange meter over havet befinner du deg nå?\n"))

# utregning; prosent-andel av hvor høyt vi er - iforhold til toppen av Mount-everest.
# Notat: Jeg har valgt å runde av til 2 desimaler med bruk av funksjonen "round()"
# prosent = round(b_moh / mount_e * 100,2)

# Skriv ut: "Du befinner deg: " x antall meter" av høyden til toppen til Mount everest:
# print('"Bleep-bleep, I am robot".. \nDu befinner deg.. \nCalculating..\n',prosent, "% av toppen av Mount-Everest (8849 moh.) ved høden:", b_moh)

# ---------------------------------------------------------------------------------
# underveisoppgave 2.6: Rett opp feilene:
# 
# høyde = 3480
# prosentAndel = høyde/8848
# print("Du er på", prosentAndel "prosent av Mount Everest ved", høyde, "meter")

# Svar:
#
# høyde = 3480
# prosentAndel = (høyde / 8849 * 100) <-- Jeg ville også ha brukt round() for å limitere antall desimaler.
# print("Du er på:", prosentAndel, "prosent av Mount everes ved", høyde, "meter")
# ----------------------------------------------------------------------------------
#
# 2.11 Moduler og pakker:
# Les docs.python.org/3/library for en oversikt over alle innebygde funksjoner og moduler som kommer med Python. (denne oppdateres for hver nye versjon av Python du har installert)
#
# Eksempler:
# import calendar as cl  #importerer modulen, og gir den et eget kallenavn "cl"
# from calendar import * # importerer alle funksjoner fra modulen "datetime" ved bruk av * som betyr "wildcard"

# Hente ut ukedagen fra en dato: tilfeldigvis datoen jeg ble født:
# weekDays = ("Mandag","Tirsdag","Onsdag","Torsdag","Fredag","Lørdag","Søndag")

# dag = cl.weekday(1991,12,4) #formatet er på year/month/day, returnerer et tall fra 0-6. 0 er Mandag, 6 er Søndag
# ukedag = weekDays[dag] # Setter tallet vi får tilbake fra "dag" til verdi funnet i array "WeekDays"
# print(ukedag) 

# fremmover kommer boka til å benytte seg av spesielt 2 moduler: "numpy" og "matplolib.pyplot"
# Disse blir importert på følgende måte:
# import numpy as np
# import matplotlib.pyplot as plt
# t = np.linspace(0,2,20)
# A = np.sqrt(t)
# plt.plot(t, A)
# plt.show()

# Jeg har brukt pip for å installere numpy og matplotlib. #MadSkillz
#
# # 2.12 Feilsøking
#
# HUSK: Det er både lov og lurt å feile!
# --------------------------------------------------------------------------------------------------------------------------
# 1. Les feilmeldingene nøye. Det henvises her ofte til både den aktuelle linja og hva slags type feil vi har med å gjøre!
#
# 2. Har du et langt program, kan det være lurt å skrive ut variablene som du lager i starten eller i midten av programmet
#    for å undersøke/teste om de har blitt laget slik som du ønsker. (Test stuff underveis, ikke skriv mye kode uten å teste.)
#
# 3. Kommenter ut dele av koden. Da kan du undersøke den koden som er igjen for å se om feilen ligger der.
#
# 4. Dersom du før feilmelding på en bestemt linje, kan det hende feilen ligger i linja over! Dette er fordi en feil i linja
#    over kan føre til at datamaskinen tror at programmet fortsetter på linja under, og at det er her feilen ligger.
#
# 5. Spør noen om å lese gjennom programmet ditt. En blir like blind på sitt eget program som en kan bli på sine egne tekster.
#    Sammarbeid er viktig i programmering!
# 
# 6. Søk opp dokumentasjon på internett! Det finnes antakelig noen som har lurt på det samme som deg. 
#    Søk på engelsk først, da dette ofte gir best resultater. En god side er www.stackoverflow.com
#
# 7. Forklar høyt for noen andre hva programmet ditt gjør, linje for linje. Dersom du ikke har noen andre tilgjengelig, 
#    kan det hjelpe å snakke høyt, f.eks. til en badeand!
# 
# 8. Gå og finn på noe annet, og kom igjen senere. En forfriskende joggetur, en kopp kaffe foran peisen eller en god bok kan 
#    klarne hodet og gjøre deg klar for nye frustrasjoner!
# 
# ----------------------------------------------------------------------------------------------------------------------------- 
# Kap 1-2. Oppsumering:
#
# * Sentrale datatyper: Heltall, flyttall, strenger.
# * Hvordan vi deklarerer variabler.
# * Hvordan vi bruker kommentarer i koden.
# * Output til konsoll.
# * Input fra bruker.
# * Hvordan vi lager og behandler lister.
# * Hvordan vi importerer moduler/bibloteker/pakker.
# 
# De viktigste kommandoene og funksjonene vi har sett på er:
# print()
# input()
# int(), float(), str()
# # <-- kommentarer
# ""  og ''
# list.append(element)
# list.remove(element)
#
#
# ___________________  ___________
# \_   _____/\_____  \ \_   _____/
#  |    __)_  /   |   \ |    __)  
#  |        \/    |    \|     \   
# /_______  /\_______  /\___  /   
#         \/         \/     \/ 
# End OF File...
