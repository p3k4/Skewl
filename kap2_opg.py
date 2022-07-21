from fractions import Fraction
# Oppgaver kapittel 2.
# Tall og variabler:

# Oppgave 1: Hva er forskjellen og likhetene mellom en variabel i matematikk og en variabel i programering?
# Svar: 
# 
# Forskjeller: I matematikken er en variabel en ukjent verdi.
# I programmering er en variabel en verdi som kan endres, 
# avhengig av betingelser eller informasjon som sendes til programmet.
# I programering ønsker vi å holde på verdier utover bare tall, men også andre datatyper som string og objekter.

# Likheter:
# Vi ønsker å holde på/ta vare på en verdi og bruker variabler til dette i 
# både matematikken og programering.

# Oppgave 2: Lag et program som legger sammen to variabler. Programmet skal så skrive ut summen.
#def addere(a,b):
#    return (a + b)
#print(addere(2,5))

# Oppgave 3: jeg tror det blir "6"
# a = 2 
# a = a + 1
# b = 2 * a
# print(b)

# Oppgave 4: Hvilke forskjeller mellom matematiske variabler og programmeringsvariabler kan du beskrive ut fra kodesnutten ovenfor? 
# Hvilke av operasjonene ovenfor gir mening matematisk, og hvilke gir ikke.
# Svar: Se første angitte svar i oppgave 1.

# Oppgave 5:  Prøv og gange sammen en variabel som er en stren (tekst), med en variabel som er et heltall. Skriv ut dette produktet og kommenter svaret.
# a = "Hei på deg fin fluesopp\n"
# print(3 * a)
# output: Hei på deg fin fluesopp Hei på deg fin fluesopp Hei på deg fin fluesopp
# Intressant, dettte viste jeg ikke ville skje! Outout blir altså strengen skrevet 3 ganger.

# Oppgave 6. Hva regner programmet nedenfor ut? Hva brukes operatoren ** til?
# tall1 = 2
# tall2 = 4
# print(tall1**tall2)

# svar: 16. "**" betyr potens! Altså, 2^4, eller 2E4 om man vil; 2 er gruntallet, 4 er eksponent.

# Oppgave 7. Lag et program som regner ut arealet av en sirkel gitt pi og radius.

# Svar:
# Skisse av programmet:
# Spørre bruker om radius på sirkelen.
# variabel som holder på verdien av "pi"
# variabel som holder på verdien av radiusen på en sirkel.
# return/print av utregningen

# def calch():
#    print("Hei, jeg heter Calch og regner ut arealer av sirkler!\n") # Velkomst til programmet!
#    radius = float(input("Skriv radius på sirkelen din!\n")) # Ber bruker om input. Dette skal benyttes til utregning, må derfor "castes" fra string til flyttall, ved bruk av float.
#    pi = 3.14    # Pi
#    a = round(pi * radius ** 2, 2) # Utregning utregning (A =3.14 * R^2)
#    print("Arealet på en sirkel med radius", radius, "er:\n",a) # Output utregningen. Ferdig ferdig, kom å tørk!
# calch()

# 8. Programmet nedenfor skal regne ut kvadratrota av et tall ved å benytte sammenhengen mellom kvadratrøtter og eksponenter, med det har tre feil!
# Rett opp programmet slik at det gir riktig svar.

# Kode:
# tall = 16
# kvadratrot = tall **1/2
# print("Rota av", Tall, "=" kvadratrot)
#
# Kode rettet opp:
# tall = 16
# kvadratrot = tall**0.5 # 1 feil: 1/2 blir ikke riktig å skrive, det må stå "0.5"
# print("Rota av", tall, "=" , kvadratrot) # 2 feil: "tall" var skrevet med stor bokstav, og det manglet et komma mellom "=" og "kvadratrot"

# 9. Lag et program som viser at kvadratrota av et tall, er den motsatte operasjonen av å opphøye et tall i 2 (kvadrere)

# Skisse:
# En funksjon som tar imot ett tall.
# Tallet skal både brukes for å regne ut kvadratroten, 
# og kvadrere (opphøyd i 2)

# def dostuff():
#    print("Hei, jeg er dostuff, og jeg skal vise at å regne ut kvadratrot er det motsatte av å kvadrere!\n")
#    tall = float(input("Skriv et tall\n"))
#    kvadrot = round(tall**0.5,2)
#    print(kvadrot,"er å dele tallet", tall, "i to like store deler.\nDefinisjon av kvadratrot:\n\"Et tall som produserer et angitt antall når det multipliseres med seg selv\".\n")

#    kvadere = round(tall**2,2)
#    print(kvadere, "er verdien vi får etter å gjøre det vi kaller \"å kvadere\" tallet",tall, "\nDefinisjon: \"Kvadrere er i matematikken å opphøye et tall eller matematisk uttrykk i 2. potens\".")
# dostuff()
#
#-------------------------------------------------------------------------------------------------------------------------------------
#
#  Oppgave 10: Regn ut følgende utrykk for hånd og i Python.
# a)   1+2*3  | d) (1+2)/3
# b)  (1+2)*3 | e) 3(2+2/2) + 4/2 
# c)  1 + 2/2 | f) 2(2+1)^2
#
# Svarene utregnet for hånd:
# a) 7 | d) 1
# b) 9 | e) 1
# c) 2 | f) 18

# Svarene utregnet med Python:
# a) print(1+2*3) = 7     | d) print((1+2)/3)
# b) print((1+2)*3) = 9   | e) print(3 * (2+2/2) + 4/2) <-- Her må stykke skrives med * tegn før parantesen.
# c) print(1+2/2) = 2     | f) print(2 * (2+1)**2)  <-- Her måtte potensen skrives med ** etter parantesen, og * tegn før parantesen.
#
#---------------------------------------------------------------------------------------------------------------------------------------
#
# Oppgave 11: 
# Lag et program som regner ut: (se bok side 38, dette er brøk).
# Kontroller ved å regne ut for hånd. Var det noe du måtte passe spesielt på i koden din?
#
# Svar: 
# def utregning_1():
#    a = -3+(Fraction(1-9, 4))+ (Fraction(4,12-3*2))
#    print(a)
# utregning_1()
#
# Jeg søkte på nettet og fant et bibliotek/modul som lar oss regne ut brøker. 
# Jeg måtte passe ekstra på å skrive regnestykket riktig, paranteser, operatorer og slik.
#
# Oppgave 12:
# Lag et program som skriver ut de firste første kvadrattallene og deretter skriver ut kvadratrota av dem.
# Notat: Kvadrattall er alle tall fra 1 og opp, opphøyd i 2

# Skisse:
# de fire første kvad.tallene
# legg disse i en array/liste
# kvradratroten av de fire første kvad.tallene
# Legge dette i liste nr. 2

# def kvad():
#    liste_1 = [] # Array for kvad.tall
#    liste_2 = [] # Array for kvadratrot-tall
#
#    tall_1 = 1**2 # Finner de fire førte kvad-tall
#    tall_2 = 2**2
#    tall_3 = 3**2
#    tall_4 = 4**2

#    liste_1.append(tall_1) # Putter kvad-tall i liste_1
#    liste_1.append(tall_2)
#    liste_1.append(tall_3)
#    liste_1.append(tall_4)

#    tall_5 = int(liste_1[0]**0.5) # Finner de fire første kvad-tallene sin kvadratrot, hentet fra liste_1
#    tall_6 = int(liste_1[1]**0.5) # Legger også til at disse skal være int
#    tall_7 = int(liste_1[2]**0.5)
#    tall_8 = int(liste_1[3]**0.5)
    
#    liste_2.append(tall_5) # Putter kvad-tallenes kvadratrot i liste_2
#    liste_2.append(tall_6)
#    liste_2.append(tall_7)
#    liste_2.append(tall_8)
    
#    print(liste_1) # Printer ut listene.
#    print(liste_2)
# kvad()

