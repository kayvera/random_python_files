#from car import Car, ElectricCar

#my_beetle = Car('volkswagon','beetle', 2016)
#print(my_beetle.get_descriptive_name())

#my_tesla = ElectricCar('tesla','roadster',2016)
#print(my_tesla.get_descriptive_name())

##or 

#import car

#my_beetle = car.Car('volkswagon','beetle', 2016)
#print(my_beetle.get_descriptive_name())

#my_tesla = car.ElectricCar('tesla','roadster',2016)
#print(my_tesla.get_descriptive_name())

#from car import Car

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagon','beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
