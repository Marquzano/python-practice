# you can import as many classes as you need
# into a program file.

# you import multiple classes from a module by
# separating each class with a comma. Once you've
# imported the necessary classes, you're free to
# make as many instances of each class as you need

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
print("\n")

# you can also import an entire module and then
# access the classes you need using dot notation
# this approach is simple and results in code
# that is easy to read.

import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# you can import every class from a module using
#  `from module_name import *`
# this method is not recommended for two reasons
# firts, it's helpful to be able to read the import
# statements at the top of a file and get a clear
# sense of which classes a program uses
# secondly, if you accidentally import a class
# with the same name as something else in your
# program file, you can create errors that are
# hard to diagnose

# if you need to import many classes from a module,
# you're better off importing the entire module
# and using the `module_name.class_name` syntax