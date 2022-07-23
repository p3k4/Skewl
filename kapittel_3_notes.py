#---------Importeringer-----------|
import os
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