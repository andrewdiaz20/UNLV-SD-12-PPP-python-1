class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

  gravity = -9.8

class Race:
  def __init__(self, name, driver_limit):
    self.name = name
    self.driver_limit = driver_limit
    self.drivers = []

  def add_driver(self, driver):
    if len(self.drivers) < self.driver_limit:
      self.drivers.append(driver)

  def get_average_ranking(self):
    total = 0
    for driver in self.drivers:
      total += driver.ranking

    return total / len(self.drivers)

class Driver:
  number_of_drivers = 0
  def __init__(self, name, age, ranking):
    self.number_of_drivers += 1
    self.name = name
    self.age = age
    self.ranking = ranking

  def get_ranking(self):
    return self.ranking

d1 = Driver('Lewis Hamilton', 36, 83)
d2 = Driver('Eliud Kipchoge', 36, 95)
d3 = Driver('Sebastian Vettel', 34, 76)
d4 = Driver('Ayrton Senna', 34, 99)

my_course = Race('Seattle 500', 4)

my_course.add_driver(d1)
my_course.add_driver(d2)
my_course.add_driver(d3)
my_course.add_driver(d4)
print(my_course.get_average_ranking())

# myCar = Car('Kitt', 180)
# myOtherCar = Car('Speedy', 55)

# print(my_course.name, my_course.driver_limit, my_course.drivers)

# myCar.talk('Michael')
