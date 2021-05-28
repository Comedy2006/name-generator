#You need to have 'names' installed
#Windows: pip install names
#Linux: sudo pip intall names
#This is a simple program, I programed it in 10 minutes and I think I will update it

import names
import random
from pyfiglet import figlet_format
from termcolor import cprint 

print("https://github.com/Comedy2006 \n")

cprint(figlet_format('\nName Generator\n', font='starwars'),
       'white', attrs=['bold'])

namegen = ''
name = ''
press = ''
randomage = 0
cons = ''

def namegenerator():
    namegen = input("Do you want a male (m), female (f) or doesn't it matter (r) name?\n")

    randomage = random.randint(18, 70)

    if (namegen == 'm'):
        name = names.get_full_name(gender='male')
        print("\n", name, ", Age:", randomage)
    elif (namegen == 'f'):
        name = names.get_full_name(gender='female')
        print("\n", name, ", Age:", randomage)
    elif (namegen == 'r'):
        name = names.get_full_name()
        print("\n", name, ", Age:", randomage)
    else:
        print("Please enter m, f or r")
        namegenerator()
    cons = input("\nDo you wanna have another name? (y for yes, n press ENTER)")

    if cons == 'y':
        namegenerator()
    else:
        exit()
namegenerator()
press = input("Press ENTER to exit.")
exit()
