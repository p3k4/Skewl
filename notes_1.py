# tall, variabler, lister av tall og av andre verdier.

# variabler eks. 1
# jeg slenger også med datatyper som er veldig vanlige å forholde seg til.

from turtle import clear

a = 10 # int (haltall)
b = 3.14 # float (desimaltall)
c = "Summer er" # string (tekst)

#print(c, a + b)

#underveisoppgave 2.1: Flyttall og desimaltall. Hvorfor blir dette feil?
print((0.1 + 0.2) * 3)

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
d = 1.4 * 10E12
print(d)

# OBS!
# Det er verdt å merke seg, at Python (som er så lur.. hihi) tolker alle tall som oppgis på standardform som et flyttall (float)
# også hvis tallet i utgangspunktet er et heltall!
# Kan likevel "caste" for å tvinge frem en annen datatype.
e = int (10E0)
print(e)

# Variabler
# * Kan ikke begynne med et tall, eller inneholde et punktum, komma eller binnestrek (understrek funker derimot fint-fint)
# Opprettelse av variabler kan se slik ut:
#x = 5
y = 2
z = x + y
print(z)

# = er ikke å tolke på samme måte som en matematisk-likning. Viktig å huske på.
i = 5
j = i + 10

# = betyr "tilordning".
# == betyr "nøyaktig verdi"
# === betyr "samme plass i minne"

# Hvilke utfordringer og muligheter gir det at bruken av likhetstegnet er forskjellig i matematikk og programmering?

# Utfordringer: Noobs need 2 get gud
# Muligheter: Verdensherredømme.

# Casting
tall = 3 # et heltall (int)
tekst = str(tall)
print(tall) # int verdi
print(tekst) # stringverdi

#fancy stuff 4 nørds:
m = 4.0
v = 2.0
k_e = 0.5*m*v**2 #akkurat.. "**" betyr potens!
print("Den kinetiske energien er:", k_e, "joule") 

#string
# "" brukes for å understreke teksten mht. skriveregler. F.eks. ironi
# ' ' brukes for streng-verdi
# string forkortes til "str"
beskjed1 = 'Jeg er "kulere" enn deg'
beskjed2= 'den er grei!'
print (beskjed1, "\n", beskjed2)

# Boolske variabler: True / false
# print()
a_1 = 1
b_1 = 3 
c_1 = 4

print(a_1 == b_1) # false
print(b_1 < a_1) # flase
print(b_1 > a_1 and b_1 > c_1) # false
print(b_1 >= a_1) # true
print(b != a_1) # true
print(b_1 > a_1 or b_1 > c_1) # true

#list comprehension <--- Innspill fra Ivar (hyggelig og belest utvikler fra Stavanger)
#liste = ["ola","Per","Kari"]
#for i in liste:
#    print(i)

# print([(x + "smith") for x in liste if len(x) > 3])

# Aritmetikk
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
