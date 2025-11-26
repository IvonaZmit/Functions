import random
from operator import length_hint

#Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.
print('-----1-----')
def sumavimas(a,b):
    print(a + b)

sumavimas(5,6)

print()
#Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
print('-----2-----')

def PISq():
    return 9.8596

print(PISq())

print()
#Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
print('-----3-----')

def sandauga(a,b):
    return a * b

print(sandauga(5,6))

print()
#Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
print('-----4-----')

def print_arr(abcde):
    for skaicius in abcde:
        print(skaicius, end=' ')
    print()

kintamasis= [1,10,7,8,6,9]

print_arr(kintamasis)

print()
#Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų. Funkcija priima tris kintamuosius,
# min, max ir length reikšmėms nustatyti.
print('-----6-----')

def random_masyvas(min, max, length):
    array = [random.randint(min, max) for i in range(length)]
    return array

arr = random_masyvas(5,6, 3)
print(arr)

#Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį),
# susumuotų ir gražintų reikšmę.
print("----------7---------")

def sum_array(random_masyvas):
    suma = 0
    for x in random_masyvas:
        suma += x
    return suma

print(sum_array(arr))

#Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.
print("----------8---------")

def avg_array(random_masyvas):
    return sum_array(arr)/len(random_masyvas)

print(avg_array(arr))

#Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.
print("----------9---------")

def print_rectangle(rows, cols):
    for i in range(rows):
        for k in range(cols):
            print('*', end='')
        print()

print_rectangle(3,4)

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print('---------10---------')

def count_chars_space(sentence):
    space = 0
    symbol = 0
    for i in sentence:
        if i == ' ':
            space += 1
        else:
            symbol += 1
    print('Simboliu yra: ', symbol, ', Tarpu yra: ', space)

sakynis = "Šiandien labai graži diena"
count_chars_space(sakynis)

#Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės.
# Pvz “Naglis” turi gautis “silgaN”.
print('---------11---------')

def reverse(sentence):
    sentence = sentence[::-1]
    return sentence

sakynis = "Naglis"
print(reverse(sakynis))

#Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą
print('---------12---------')

def reverse2(sentence):
    return sentence[::-1]

sentence = "Labas rytas"
print(reverse(sentence))

#Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
print('---------13---------')

def numbers(array):
    skaitmenys = []
    skaiciai = "0123456789"
    for z in array:
        if z in skaiciai:
            skaitmenys.append(z)
    print(f"Skaiciai masyve: {skaitmenys}")

array = "rytoj reikia atsikelti 7:00, kad spet i darba 8val."
numbers(array)

#Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius. (jei pavyks, patobulinkite, kad
#funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.
print('---------14---------')

def numbers2(array2, sveikieji=True):
    for z in array2:
        if sveikieji and isinstance(z, int):
            print(z)
        elif not sveikieji and isinstance(z, float):
            print(z)

duomenys = [1, 2.5, "labas", 7, 3.14]
numbers2(duomenys, True)

#Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
print("----------15--------")

def word_count(sentence):
    return len(sentence.split())

tekst = "Krenta sniegas"

print(word_count(tekst))


#Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean. Funkcija gražina prafiltruotą masyvą.
# Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.
print('---------16---------')

def filtruoti_skaicius(skaiciai, tik_poriniai):
    if tik_poriniai:
        return [x for x in skaiciai if x % 2 == 0]
    else:
        return [x for x in skaiciai if x % 2 != 0]

print(filtruoti_skaicius([1, 2, 3, 4, 5, 6], True))
print(filtruoti_skaicius([1, 2, 3, 4, 5, 6], False))


#Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.
print('---------17---------')

def number_is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(number_is_prime(10))
print(number_is_prime(7))

#Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.
print('---------18---------')

def pakelti_laipsniu(a,b):
    return a ** b

print(pakelti_laipsniu(2, 3))
print(pakelti_laipsniu(5, 2))

#Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik skirtingus elementus.
print('---------19--------')

def skirtingi_elementai(array):
    unikalus = []
    for x in array:
        if x not in unikalus:
            unikalus.append(x)
    return unikalus

print(skirtingi_elementai([1,2,3,3,4,5,5,6]))

#Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.
print('---------20--------')

def daug_pasikartojantis_simb(tekstas):
    daznis = {}
    for s in tekstas:
        daznis[s] = daznis.get(s, 0) + 1
    daugiausia = max(daznis, key=daznis.get)
    print(daugiausia)

daug_pasikartojantis_simb("viso gero")


#Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.
print('---------21--------')

def ilgiausias_zodis(tekstas):
    zodziai = tekstas.split()
    ilgiausia = max (zodziai, key=len)
    print(ilgiausia)

ilgiausias_zodis("Labas vakaras")

#Sunkesni
#Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir
# gale. PVZ (---labas---)
print('-------1------')

def spausdinti_su_bruksniais(tekstas):
     print(f'----{tekstas}----')

spausdinti_su_bruksniais("Labas")

#Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu.
# Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].
# (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)
print('-------2-------')

def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

