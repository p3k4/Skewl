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
sum_it_3()
