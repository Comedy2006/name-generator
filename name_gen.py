#You need to have 'names' installed
#Windows: pip install names
#Linux: sudo pip intall names
#This is a simple program, I programed it in 10 minutes and I think I will update it

import names

namegen = ''
name = ''

def namegenerator():
    namegen = input("Do you want a male (m), female (f) or doesn't it matter (r) name?\n")

    if (namegen == 'm'):
        name = names.get_full_name(gender='male')
        print(name)
    elif (namegen == 'f'):
        name = names.get_full_name(gender='female')
        print(name)
    elif (namegen == 'r'):
        name = names.get_full_name()
        print(name)
    else:
        print("\nPlease enter m, f or r")
        namegenerator()
namegenerator()
