import datetime
import random

from polite import *
# import polite
from random import randint


def say_hi(): #nieko nepriima, nieko negrazina
    print("hi")

say_hi()
say_hi()
say_hi()

def say_hi_to(name):#priima, nieko negrazina
    print(f'hi {name}')

say_hi_to("Jonas")
say_hi_to("Janina")

vardas = "Viktoras"
say_hi_to("Viktoras")

def sim_pi():# nieko nepriima, grazina reiksme
    return 3.1415

res = sim_pi()
print(res)

print(sim_pi())

def sumavimas(a,b):#kazka priima, grazina rezultata
    return a + b

res = sumavimas(40,80)
print(res)

def calc_age(birth_year):
    return datetime.date.today().year - birth_year

mano_metai = 1995

my_age = calc_age(mano_metai)

print(my_age)

def make_initials(name,surname):
    return (name[0] + surname[0]).upper()

print(make_initials("Naglis","Mockevičius"))
print(make_initials("Naglis","mockevičius"))

def make_initials_v2(full_name):
    names = full_name.split()
    initials = ""
    for pt in names:
        initials += pt[0]
    return initials.upper()


person = "Joana jakaterina Mažena Jokubov"

res = make_initials_v2(person)
print(res)


zmones = ["Jonas Antanavicius", "Jokubas Valudok", "Zigmantas Peima"]

for per in zmones:
    print(make_initials_v2(per))

def print_info(name = "", surname = "", birth_year = 0): #tai i ka funkcija priima reiksmes yra arguments
    print(f"Mano vardas yra {name}, pavarde {surname}. Gimimo metai {birth_year}")


print_info("Naglis","Mockevičius",1990)
print_info("Naglis","Mockevičius")
print_info("Žemaitė", birth_year=1873)

print(1,1,1,2,5,4,7,8,9, sep="", end="\n")




def be_polite():
    good_morning()
    good_day()
    good_evening()
    good_night()

print( be_polite() )
# be_polite()


print(randint(14,40))



def student_grades_avg(student_grades):
    sum = 0
    for st_grade in student_grades:
        sum += st_grade
    return round(sum / len(student_grades))

def arr_avg_round(arr):
    sum = 0
    for num in arr:
        sum += num
    return round((sum/len(arr)))
