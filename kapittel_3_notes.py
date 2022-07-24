#---------Importeringer-----------|
import os
from re import X
def clear():                     
    os.system('cls')
#---------------------------------|

# Kapittel 3; Kontrollstrukturer og funksjoner!
# Notater og kode skrevet av Per Christian Veien, 
# innhold hentet fra boken 9788215034287.

# Hva er kontrollstruktruer og funksjoner?
# Svar: "Vi bruker kontrollstrukturer når vi ønsker å 
# gjøre noe flere ganger uten at vi må skrive en linje
# kode for hver gang den skal gjøre det!". Disse heter "løkker".

# Og, det er strukturer som gjør at datamaskinen kkan velge å enten 
# utføre eller hoppe over linjer med kode basert på en eller annen "tilstand" i programmet.
# F.eks. verdien til en variabel. Dette kalles "vilkår" eller "betingelser", 
# og kjennetegnes gjerne ved bruk av "if-setninger"
 
# Hva er en funksjon?
# Svar: Funksjoner lar oss gruppere kodelinjer som "hører sammen" og utfører en oppgave i fellesskap.
# Betlingelser ved bruk av betingelser: (if, elif, else), og tilstand (">", "=="):

def sjekk_1():
    clear()
    tall_1 = float(input("Skriv inn et tall\n"))
    if tall_1 > 0:
        print(tall_1, "er et positivt tall!\n")
    elif tall_1 == 0:
        print("Skriv et annet tall..\n")
        sjekk_1() # hit me baby one more time!
    else:
        print(tall_1, "er et negativt tall\n")
#sjekk_1()

#Vi kan også bruke flere "if"-setninger sammtidig for å sjekke flere betingelser samtidig (uvanlig fra andre prog.språk)!
def sjekk_2():
    clear()
    tall_1 = float(input("Skriv et tall\n"))
    if tall_1 > 0:
        print("Tallet er possitivt!")
    if tall_1 == 10:
        print("Tallet er også 10!")
#sjekk_2()

# Hvis vi vil at kun en betingelse skal inntreffe, kan vi bruke elif i kombinasjon med if:
# Legg merke til at dersom vi skriver tallet "4" - vil første "treff" på betingelsene våre være den som kjøres.
# Andre betingelser i "elif" vil ikke evalueres/være gjellende dersom betingelsen av if først er sann!  
def sjekk_3():
    tall_1 = float(input("Skriv et tall\n"))
    if tall_1 < 5:
        print("Tallet",tall_1,"er mindre enn 5")
    elif tall_1 < 20:
        print("Tallet",tall_1,"er mindre enn 20")
#sjekk_3()

# Repetisjon: La oss si vi gjør det samme her (skriver tallet 4), men nå med kun if setniger:
# Her vil begge betingelsene være gjellende frem til vi bruker tallet 5, eller et tall større enn 20. 
def sjekk_4():
    tall_1 = float(input("Skriv et tall\n"))
    if tall_1 < 5:
        print("Tallet",tall_1,"er mindre enn 5")
    if tall_1 < 20:
        print("Tallet",tall_1,"er mindre enn 20")
#sjekk_4()

# Videre utforsking av dette, med bruk av "elif"
# Flaks for oss kan vi bruke så mange "elif" vi ønsker oss.
# I andre språk er det kun en "if", jeg får se om det lønner seg å fortsette med eller ikke etterhvert som jeg lærer meg mer.
def sjekk_5():
    tall_1 = float(input("Skriv et tall\n"))
    if tall_1 < 5: # logisk sammenlikning (sjekker "tilstand" av en variabel)
        print("Tallet er veldig lite")
    elif tall_1 < 20:
        print("Tallet er ganske lite")
    elif tall_1 < 50:
        print("Tallet er nokså lite")
    elif tall_1 < 100:
        print("Tallet er ikke så lite")
    else: #Legg merke til her, "else" benytter ingen logisk sammenliking som if eller elif.
        print("Tallet er faktisk ganske svært!")
#sjekk_5()

#----------------------------|
# Repitisjon av operatorer:  |
# Symbol | Betydning         |
#    >   | Større enn        |
#    <   | mindre enn        |
#    ==  | er lik            |
#    !=  | er ikke lik       |
#    <=  | mindre eller lik  |
#    >=  | større eller lik  |
#----------------------------|

# Bruk av flytskjemaer:
# Jeg laget et flytskjema over alminnelig arbeidstid på draw.io
# link: https://github.com/p3k4/Skewl/blob/main/flytskjema.drawio

# Når mulighetene er vurdert ferdig og satt opp på et flytskjema, kan vi "oversette" det til kode:
def working_grunt():
    print("I'm Hellgrom, a happy grunt!\n")   # Begynner programmet.
    stat = float(input("what time is it?\n")) # Spør bruker om input
    if stat < 6.30:                           # Natt
        print("I'm sleeping, zzz,Zzz\n")      
    elif stat == 6.30:                        # Begynner på jobb
        print("Work-work-work.")        
    
    elif stat < 15.00:                        # Jobber dagskift
        print("I'm working daytime shift!")
    elif stat == 15.00:                       # Ordinær arbeidsdag over
        print("I usually go home from work now.")
    
    elif stat < 16.00:                        # Første time utover normal arbeidsdag
        print("Seems I'm gonna work some overtime!")
    elif stat == 16.00:                       # Overtids arbeid har begynt
        print("I'm gonna work some overtime now.")
    
    elif stat < 21.00:                        # Allmennelig overtid
        print("I'm working overtime!")
    elif stat == 21.00:                       # Grensen for lovelig/ulovelig overtid
        print("Enough work for one day..")
    else:
        print("What?!\n")                     # Reaksjon for alt annet enn gitte sammenlikninger ^__^     
#working_grunt()

# Flytskjema de brukte i boken:
# https://github.com/p3k4/Skewl/blob/main/ph-diagram.drawio

# "Oversatt til kode"
def ph_sjekk():
    ph = float(input("Hva er pH-verdien i løsningen?\n"))
    if ph > 7:
        print("Løsningen er basisk")
    elif ph < 7:
        print("Løsningen er sur")
    elif ph == 7:
        print("Løsningen er nøytral")
#ph_sjekk()

# Intervaller! Woo-hoo!
# Dersom vi ønsker å bruke flere vilkår i samme sammenlikning, kan vi bruke operatorne "and" eller "or".
# Hm, hvorfor finnes ikke "between"?

def sjekk_6():
    tall = float(input("Skriv inn et tall\n"))
    if tall < 42 or tall > 42:
        print("Tallet er større eller mindre enn \"42\"")
    if tall > 42 and tall < 100:
        print("Tallet ligger i intervallet (42,100)")
# sjekk_6()

# Underveisoppgave 3.1
# Lag et program som tar alderen til brukere som input. Programmet skal evaluere alderen til
# personen ved å skrive ut utlike melinger alt ettersom hvilket aldersintervall alderen ligger innenfor.
# Legg til så mange vilkår som du ønsker.

# Valgte vilkår     outputs
# < or == 1       : Velkommen til verden lille du!
# < or == 5       : Nyt tiden frem til du skal på skolen. Lær deg å telle, tegne og snakke
# < 13            : Fortsett å lær deg nye ting, og bli bedre til det du allerede kan!
# == 13           : Du kan nå lovelig bestemme din egen hårsveis!
# == 14           : Fjortis-fjortis!
# > 12 and < 19   : Du er tennåring, og skal være det i x antall år til!
# == 16           : Det er nesten sant at du kan nå kjøre moped, lett-motorsykkel og begynne øvelseskjøring!
# == 18           : Du er nå mynding 
# < 30            : Du har ennå ikke nådd din beste alder!
# == 30           : Du har nådd din beste alder!
# else:           : Du er for gammel til å bruke dette programmet!

def alder():
    age = int(input("Hvor gammel er du?\n"))
    if age < 1 or age == 2:
        print("Velkommen til verden lille du!")
    elif age < 5 or age == 5:
        print("Nyt tiden frem til du skal på skolen. Lær deg å telle, tegne og snakke.\nHa det trygt, godt og gøy!")
    elif age < 13:
        print("Fortsett å lær deg nye ting, og bli bedre til det du allerede kan!")
    elif age == 14:
        print("Fjortis-fjortis!")
    elif age > 12 and age < 19:
        rem = 19-age
        print("Du er tennåring, og skal være det i",rem,"år til!")
    if age == 16:
        print("Det er nesten sant at du kan nå kjøre moped, lett-motorsykkel og begynne øvelseskjøring!")
    elif age == 18:
        print("Du er nå mynding")
    elif age < 30:
        print("Du har ennå ikke nådd din beste alder!")
    elif age == 30:
        print("Du har nådd din beste alder!")
    else:
        print("Du er for gammel til å bruke dette programmet!")
#alder()

# Figur 3.2 Gjenskapt i et diagram for draw.io (kan fritt importeres)
# https://github.com/p3k4/Skewl/blob/main/andregradslikninger-diagram 
# Legg merke til koeffisentene a,b,c i diagramet
#
# Underveisoppgave 3.2 utgave 1:
def likning_1():
    a = float(input("a =\n"))
    b = float(input("b =\n"))
    c = float(input("c =\n"))

    rot = b**2 - 4*a*c
    if rot > 0:
        print("Vi får to løsnigner!")
    elif rot == 0:
        print("Vi får én løsning!")
    else:
        print("Vi får ingen reelle løsninger..")
# Poenget er ikke å løse andregradslikninger - kan kan vi gjøre for hånd eller på en kalkulator. 
# Hvilke didaktiske fordeler kan det være med å programmere andregradsformelen?
#
# Svar: Vel, jeg er ikke stødig i andregradslikninger. Så det er bra for meg å få repetert slikt,
# på en annen side er det nok god trening for å utvikle programmer som støtter seg på matematikk generelt.
# Det må taes noen hensyn og slik når man skal "oversette" formler til kode. Det er alltid gøy å få til på egenhånd.
# Enn så lenge er jeg glad jeg kan støtte meg på løsningen i boka.

def likning_2():
    print("Hei, jeg et program som løser andregradslikninger!\nFyll inn verdiene:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    
    rot = b**2 - 4*a*c
    if rot > 0:
        x1 = (-rot**0.5)/(2*a)
        x2 = (-rot**0.5)/(2*a)
        print(" Vi få to løsniger: x1 =",x1,"og x2=",x2)
    elif rot == 0:
        x = -b/(2*a)
        print(" Vi får én løsning: x=",x)
    else:
        print(" Vi får ingen reelle løsninger..")
#likning_2()

# Jeg leste litt som andregradslikninger og testet med verdiene a = 1 b = 10 og c = -24
# https://quickmath.com/ kan brukes for å sjekke om det blir riktig.
# Fra mitt øyemed spytter funksjonen hvertfall ut et svar - jeg er fornøyd, heh.

# Løkker facts:
# 1) Løkker er fett og kraftige. Use them often and with care!
# 2) I python er det 2 typer løkker: "while" og "for"
# 3) En while-løke er det vi kaller en "tilstandsløkke". Den kjører helt frem til en logisk tilstand ikke lenger er oppfylt.

# while-løkke:
def do_1():
    c = 0
    while c < 10:
        print("Yabadabbadooo!")
        c += 1 # Husk å avslutte løkka på en måte, ellers blir det nok en del spam.
#do_1()

# Gjett riktig tall og vinn en bil!
def winning():
    w_tall = 1349
    n = int(input("Gjett riktig tall og vinn en bil!\n"))
    while n != w_tall:
        print("Prøv igjen!!")
        n = int(input(""))
    clear()
    print(w_tall, "var riktig!! Gratulerer med din nye lekebil!") # inntrykk-tilbake(in lack of better words..) kjører først når løkka treffer på "sammenlikningen"
    print("        _______")
    print("       //  ||\ \"")
    print(" _____//___||_\ \___")
    print(" )  _          _    \"")
    print(" |_/ \________/ \___|")
    print("___\_/________\_/______")
#winning()

# Flere artige løsniger ved bruk av while-løkke:
# Hvor-lenge-må-jeg-spare-kalkulator:

def save_it():
    clear()
    saldo = int(input("Hva er din startkapital for sparingen?\n"))
    sum_end = int(input("Hvor mye ønsker du å spare opp til?\n"))
    r = float(input("Hva er renta?\n"))
    år = 0
    
    while saldo <=sum_end:
        saldo = round(saldo + saldo * r) # Utregning. La inn en round() for å holde styr på desimalene.
        år +=1 # For å holde styr på hvor mange år man har spart/ eller må spare.
        print("år", år, ":", saldo) # Skriver ut år man har spart, og saldo på dette året.
    print("Det tar", år, "år før du har:", sum_end, "kr.") # Skriver ut antall år og slutt-beløpet.
#save_it()   

#"for-løkker"
# Kort oppsumert: For løkker er kjekt når man vet hvor lenge løkka skal kjøre.
# Funker i prinsippet veldig likt som while-løkker. Vi trenger derimot ikke ha en egen "counter" variabel med for-løkker.
# Nedenfor er range(1,10) slik : "1" er start-verdien, "10" er sluttverdie. Itterasjonene er: sluttverdien-1
# En for-løkke er en løkke som gjentar kode. Den er vanlig å benytte sammen med en range() funksjon for telling,
# eller i kombinasjon med en liste for å iterere over elementer i lista.

# Vi mennesker kan lettere lese kode dersom variabler og funksjoner har beskrivende navn. Vi kan bruke a,b,c eller f2 og det vil fungere.
# Men, det er anbefalt å bruke beskrivende navn på funksjoner og variabler likevel.
def loop_it():
    for i in range(1,10): #Legg merke til av vi må bruke ":"
     print(i," itterasjon")
#loop_it()

#Skal vi gjøre det samme med 10 itterasjoner må sluttverdien være 11:
def loop_it_again():
        for i in range(1,11): # 1,2,3,4,5,6,7,8,9,10
            print(i, "itterasjon")
#loop_it_again()

# eksemplet fra boka side 49:
def loop_2():
    for i in range(0,5):
        print(i**2)
# loop_2()

# range() kan har 3 arumenter; start(fra og med), slutt(til men ikke med) og sist intervallet()
# La oss skrive ut alle partall mellom 0 og 20 ved bruk av alle disse arumentene:

def count_it():
    for i in range(0,21,2): # Kunne ha satt startverdien til 2, fordi vi vet at hverken 0 eller 1 er et partall.
        print(i)
#count_it()

# I matematikken kan for-løkker vistnok brukes for summerings av "rekkesummer", jeg tenker at dette peker til arrays, men - vi får se.
# Også nevner boka noe om sigma; sigma-tegnet brukes for summering mellom startverdi og N. Høres kjent ut, uten at jeg har brukt sigma før.

def loop_3():
    t = 0
    for i in range(1,6):
        t += i**2 # legger til svaret i variabel "t" for hver itterasjon
    print("Summen av kvadratet til de føreste fem tallene er:",t)
#loop_3()

# for-løkker og lister (ja, dette er mer kjent for meg).
def itter_it():
    liste = [1,10,2,4] # liste med heltall
    for i in liste: # hvor hvert element i lista
        print(i) # print elementet
#itter_it()

# Vi kan gjøre dette med alle datatyper i en liste:

def itter_it_2():
    liste = [1,"2",3.0] # liste med ulike datatyper. Ikke gjør dette (bland ulike datatyper i samme liste) selv om det funker.
    for i in liste:
        print(i)
#itter_it_2()

# Boken ønsker å ta oss tilbake til matematikken
# her et et ekemepel på for-løkker med andregrads-funksjoner:
def itter_it_3():
    liste_a = [-3.0, -2.5 , -2.0, -1.5, -1.0, -0.5, 0.0]
    liste_b = []
    for i in liste_a:
        a = 2*i**2 + 3* i + 1 # (2x^2 + 3x +1)
        liste_b.append(a) #legger svaret til i den tomme arrayen liste_b
    print(liste_b)
#itter_it_3()

# Funksjoner:
# Som Harry Potter en gang sa: functions are really the bread and butter to wizards!
# Sier meg enig der.
# Python har en rekke innebygde funksjoner, og vi kan lage våre egne (som jeg har gjort i store deler av denne fila).
# Ikke bare fordi jeg kan, men fordi det gjør det langt mer oversiktlig enn å ha en egen .py fil for hvert jævla program.

# Jeg har allerede brukt flere innebygde funksjoner:
# print()
# range()
# round()
# input()
# clear() # Denne er riktig nok laget selv, men ved bruk av en inportert modul ("os")

# En definisjon på funksjoner:
# " En funksjon er en blokk med kode som blir utført når det "kalles" på. En funksjon kan ta ingen, én eller flere parametere som imput, og returnere
# ingen, en eller flere variabler som output".

def sum_it():
    liste = [1,3,14,12,3,14,16,7,22,5,23,46]
    s_liste = sum(liste)
    return s_liste # her ønsker jeg kun å returnere en variabel
# print(sum_it()) # Funksjoner kan kjøre andre funksjoner: her er både print og funksjonen "sum_it" som jeg nettopp laget, i samme funksjon

# Det samme som funksjonen sum gjør, kan gjøres med bare en en for-løkke på flere forskjellige måter:
def sum_it_2():
    liste = [1,3,14,12,3,14,16,7,22,5,23,46]
    a = 0 
    for i in liste:
        a += i
    print(a)
#sum_it_2()

def sum_it_3():
    liste = [1,3,14,12,3,14,16,7,22,5,23,46]
    sum = 0
    for i in range(len(liste)): # range(len(liste)) betyr "lengden av lista"
        sum += liste[i] # henter verdien utifra plasseringen i array "liste" og legger til denne i variabelen "sum"
    print(sum)
#sum_it_3()

# Funksjoner continued:
# La oss si, for dere mattematikk-hoder der ute at vi har en funksjon som er slik: f(x) = x^2
# I kode kan vi lage denne andregradsfunksjonen til vår egen-hjemme-mekka funksjon:
def vår_funksjon(x):
    utregning = x**2 # dette kalles en "retur-variabel", ikke veldig viktig å kunne navnet, men forstå hensikten.
    return utregning

# Funksjonen har vi sangt skal hete "vår_funksjon" isdeden for "f"
# Den tar imot et tall, dette er "x" og kalles et "parameter".
# "utregning" er det som står etter likhets-tegnet i den matematiske funksjonen. Vi har valgt å lage dette som en variabel
# return er nesten en funksjon, men lettere forstått som et "kodeord". Her sier vi at funksjonen vår skal returnere
# verdien til variabelen "utregning". Dette er litt uvanlig iforhold til slik jeg har gjort i de fleste kode-snuttene,
# hvor jeg har brukt print() isteden. Alt til sitt bruk kan man si.

# Vi tester funksjonen med et vilkårlig tall: 3
# a = vår_funksjon(3)
# print(a)

# Nice to know: Vi "sender" argumenter(3) til funksjoner, og "definerer" parametere(x)
# Mange bruker ordet "parameter" for begge deler.

# Underveisoppgavee 3.5

# Lag en funksjon du kaller tredjegrads, som tar x som parameter og regner ut x^3. Bruk funksjonen ved å printe resultatet av åå kalle på funksjonen
# med noen forskjellige x-verdier.
def tredjegrads(x):
    utregning = x**3
    return utregning
# print(tredjegrads(3))
# print(tredjegrads(5))
# print(tredjegrads(10))

#Funksjoner behøver ikke være matematiske:
def si_hei():
    print("Hei på deg!")
#si_hei()

# Funksjoner med flere parametere:
def funk_1(x,y,z):
    a = x**2
    b = y**2
    c = z**2
    return a,b,c
# test = funk_1(2,4,6)
# print(test)

# Underveisoppgave 3.6 Fra Fahrenhei til celsius
# 1) Lag en funksjon temp_celsius som tar inn en temperatur i fahrenhei og returnerer en temeratur i celsius:

# Notat fra internett: To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by .5556 (or 5/9).
def temp_celsius(a):
    b = (a-32) * 5/9 # subtract 32 and multiply by .5556 (or 5/9).
    return round(b)
# temp = temp_celsius(50)
# print(temp)

# test med flere verdier:
temp_1 = temp_celsius(45)
# print(temp_1)
temp_2 = temp_celsius(50)
# print(temp_2)
temp_3 = temp_celsius(70)
# print(temp_3)

# 3) Hva burde vi kalle variablene slik at andre lett kan forstå hva programmet gjør?
# Svar: Jeg bruker kommentarer svært mye for å gjøre dette. Men la gå, jeg skal gjøre det mer forstårlig:

def fahrenheit_to_censius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 # Converting it like a pro
    return round(celsius)

temp_4 = fahrenheit_to_censius(45)
temp_5 = fahrenheit_to_censius(50)
temp_6 = fahrenheit_to_censius(70)
# print(temp_4,temp_5,temp_6)

# Underveisoppgave 3.7:
# For kodesnutten under, svar på følgende:
#
# 1) Hva tror du eleven har prøvd å få til?
# svar: Lage et program som løser andregradsfunksjoner.

# 2) Hva er output fra programmet?
# Svar "None", og betyr at "a" ikke har noen verdi

# 3) Hva har eleven misforstått
# Svar: Man må returnere en verdi for å få det til å fungere.

# 4) Hvordan kan vi rette opp programmet?
# Svar: Jeg har laget alle kode-snuttene under.

# Kode 1:
def f_1(x):
   y = x**2  
   return y # Feilen er at eleven aldri returnerer variebelen
# a = f(2)
# print(a)

# Kode 2:
def f_2(x):
   y = x**2  
   return y # Feilen er at eleven aldri returnerer variebelen
# a = f(2)    
# print(a)

# Kode 3:
for i in range(10):
    def f(x):
        return x ** 2
#    print(f(x)) Her er det skrevet x men når koden blir kjørt uten at x har en verdi, vil man få en nameError hvor x-verdien ikke er definert.
#                Legges det til en verdi isden, vil koden fungere helt fint - selvom jeg syntes det er rart å definere en funksjon inni en loop.

# Returvariabler:
def kvadrat_og_rot(tall):
    kvadrat_rot = tall ** 0.5
    kvadrat = tall ** 2
    return kvadrat, kvadrat_rot # Vi kan bruke flere retur variabler, nullstress joggedress.

a, b = kvadrat_og_rot(36)
#print(a, b)

# Fact: Vi kan lage funksjoner inni funksjoner!
# Mitt eget ekempel på dette, fordi jeg ikke forstår kjemi-oppgaven i boka side 58/59:

def retur_navn(navn):
    return navn

def funksjon_i_funksjon():
    navn = input("Hva heter du?\n")
    return print("Hei", retur_navn(navn)) # her vil den kjøre funksjonen over "retur_navn" for å returnere "navn"
# funksjon_i_funksjon()

# Underveisoppgave 3.9:
# Du har en liste med steder og en liste med badetemp. som du ønsker å printe ut pent i konsollen.
# Lag en funksjon "celsius_til_fahrenheit" som konverterer temperaturer fra celsius til fahrenheit. Bruk denne funksjonen inni en annen funksjon 
# "skriv_ut_temperaturer" slik at du skriver ut en liste med temeraturer i fahrenheit.

steder = ["Stavanger","Bodø","Trondheim","Bergen","Kristiansand","Oslo","Halden"]
temperaturer = [10,14,18,8,17,16,11]

# Vi er smarte og finer formelen til konverteringen: Gange med 1.8 og legg til 32
def celsius_til_fahrenheit(temp):
    celisus = (temp * 1.8) + 32
    return celisus

def skriv_ut_temperaturer(temperaturer):
    for i in temperaturer:
        måling = celsius_til_fahrenheit(i) # Her bruker jeg en funksjon inni en annen funksjon.
        print(måling)
# skriv_ut_temperaturer(temperaturer)

# Vi skal nå lage noen funksjoner til å finne parameterne til en linær matematisk funksjon fra 2 punkter på grafen til funksjonen!
# Målepunktene er: p1 = (x1,y1) og p2 =(x2,y2)
# Poenget er å vise kodeforståelse og matematiske sammenhenger til programmering!
# Dette er formelen vi skal bruke: f(x) = ax + b

# 1) Lag en funksjon som tar imot 3 parametere, og returnerer funksjons verdien
# svar:
def linær_funksjon(a,x,b):
    posisjon = a * x + b   
    return posisjon

# Test at linær_funksjon fungerer: Den funker!
# test = linær_funksjon(2,10,5)
# print(test)

# 2) Lag en funksjon som tar punktene p1 og p2 som parametere, gjerne som lister.
def finn_posisjon(liste_1,liste_2):
    x1 = liste_1[0] # første posisjon
    y1 = liste_1[1] # første posisjon

    x2 = liste_2[0] # andre posisjon
    y2 = liste_2[0] # andre posisjon

#    pos1 = (y2-y1) / (x2-x1)  Dette er matematikk.. Denne kalles topunksformelen
#    pos2 = y1-pos1 * x1       Dette er matematikk.. Denne kalles ettpunksformelen
#    return pos1, pos2

# Det er ønskelig å ha disse formlene i hver sin funksjon.

def topunktsformelen(p1,p2):
    x1 = p1[0] # første x koordinat
    y1 = p1[1] # første y koordinat

    x2 = p2[0] # andre x posisjon
    y2 = p2[1] # andre y posisjon
    pos = (y2-y1)/(x2-x1) # Matematikk magic!
    return pos

def enpunktsformelen(p1,a):
    x1 = p1[0] # første x koordinat
    y1 = p1[1] # første y koordinat
    pos = y1-a * x1 
    return pos

def finn_linær_funksjon(p1,p2):
    a = topunktsformelen(p1,p2)
    b = enpunktsformelen(p1,a)
    return a, b

# Vi lager oss noen koordinater
posisjon_1 = [3,4]
posisjon_2 = [6,2]

# Bruker koordinatene til funksjonene vi har laget.
c, d = finn_linær_funksjon(posisjon_1,posisjon_2)
#print(c, d)

e = linær_funksjon(3,c,d)
#print(e)

fe = linær_funksjon(6,c,d)
#print(fe)
