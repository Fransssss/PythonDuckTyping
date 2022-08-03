
class Car:

    def buy(self):
        print("[ You may buy a car ]")

    def drive(self):
        print("[ You may drive a car ]")


class Bicycle:

    def drive(self):
        print("[ Yes, You can cycle a bicycle! ]")


class Adult():

    def get(self, Car):
        Car.buy()
        Car.drive()


class Children():

    def get(self, Bicycle):
        Bicycle.drive()
