print(type('hello world'))

class Car:
    def __init__(self, name):
        print('hello world')
        self.name = name

    def start(self):
        print("vroom")

    def talk(self, driver):
        print(f"Greetings, {driver}. I am {self.name}.")

class RobotCar(Car):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type


my_car = Car()
my_car_2 = Car('lightning Mcqueen')
print
print(my_car)