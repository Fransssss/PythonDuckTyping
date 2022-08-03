# Author: Fransiskus Agapa

# ======================
# simple program where a person choose to get and use a vehicle
# the program would ask if the person is an adult or not
# there is limit for either the person is an adult of not
# ======================

from classes import Car
from classes import Bicycle
from classes import Adult
from classes import Children

print("\n== Get nad Use a Vehicle ==")
print("1. Car")
print("2. Bicycle")
print("e. Exit")
choice = input("choice: ").lower()

while choice != 'e':
    if choice == '1':
        print("\n-- Get a Car --\n")
        self_status = input("Are you an adult (yes/no)? ").lower()
        person = Adult()                 # assume user is an adult
        if self_status == "yes":
            print("\n")
            car_yes = Car()
            person.get(car_yes)
            print("\n")

        elif self_status == "no":
            try:
                car_no = Bicycle()
                person.get(car_no)       # Bicycle only has one method, so oython would complain
            except AttributeError:
                print("\n[ You are not allowed to buy and/or drive a car ]")

        else:
            print("\n[ Invalid response ]")

    elif choice == '2':
        print("\n-- Get a Bicycle --\n")
        self_status = input("Are you an adult (yes/no)? ").lower()
        person = Adult()                 # assume person is an adult
        if self_status == "yes":
            print("\n")
            try:
                bicycle_yes = Bicycle()   # on purpose to cause error to tell user if they are able to buy and drive bicycle
                person.get(bicycle_yes)
            except AttributeError:
                print("[ You are able to get and/or cycle a bycycle ]\n")

        elif self_status == "no":
            print("\n")
            bicycle_no = Bicycle()
            person = Children()
            person.get(bicycle_no)
            print("\n")

        else:
            print("\n[ Invalid response ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Get and Use a Vehicle ==")
    print("1. Car")
    print("2. Bicycle")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
