# ALL IMPORT STATEMENTS MUST BE MADE AT THE BEGINNING OF EACH FILE
# THE EXCEPTION IS WHEN WRITING COMMENTS THAT DESCRIBE THE WHOLE MODULE
# THE EXCEPTION IN THIS CASE BEING TO INFORM AND DEMONSTRATE THE DIFFERENT WAYS OF IMPORTING
# one advantage of functions is the way they separate blocks 
# of code from your main program. You can go a step further by
# storing your functions in a separate file called a module and
# then importing that module into your main program. An import
# statement tells Python to make the code in a module available
# in the currently running program file
# there are several ways to import a module

# a module is a file ending in .py that contains code you want
# to import into your program
# lets make a module that contains the function make_pizza()
# to make this module, we'll remove everything from the file
# pizza.py except the function make_pizza()
# (it still works with pizza.py as I have it now but I will
# make pizz_2.py to follow along with the example)

import pizza_2

pizza_2.make_pizza(16, 'pepperoni')
pizza_2.make_pizza(12, 'mushrooms', 'green peppers', 'green peppers', 'extra cheese')

# to call a function from an imported module, enter the name of
# the module you imported, pizza_2, followed by the name of the
# function, make_pizza(), separated by a dot.

# you can also import a specific function from a module
# you can also import as many functions as you want from
# a module by separating each function's name with a comma

from pizza_2 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# with this syntax you don't need to use the dot notation when
# you call a function. Becuase we've explicitly imported the
# function in the import statement, we can call it by name when
# we use the function

# when importing a function you can also use a short unique alias
# an alternate name similar to a nickname wehn you import the function

from pizza_2 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# you can also provide an alias for a module name. Giving a
# module a short alias, like p for pizza, allows you to call
# the modules functions more quickly.

import pizza_2 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# you can tell Python to import every function in a module
# by using the asterisk (*) operator

from pizza_2 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# the asterisk in the import statement tells Python to copy
# every function from the module pizza into this program file
# becuase every function is imported, you can call each function
# by name without using the dot notation
# it's best not to use this approach when you're working with 
# larger modules that you didn't write. functions with the same
# name in your main may be overwritten by the other function
# in the imported module
# the best approach is to import the function or functions you want
# or import the entire module and use the dot notation