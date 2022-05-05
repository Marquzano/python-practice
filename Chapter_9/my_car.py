from car import Car

# this file will import the Car class and then
# create an instance from that class.

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# importing classes is an effective way to program
# when you move the class to a module and import
# the module, you still get all the same
# functionality, but you keep your main program
# file clean and easy to read. You also store most
# of the logic in separate files; once your
# classes work as you want them to, you can leave
# those files alone and focus on the higher-level
# logic of your main program