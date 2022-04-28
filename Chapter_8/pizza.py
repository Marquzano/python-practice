# sometimes you won't know ahead of time how many arguments a
# function needs to accept. Python allows a function to collect
# an arbitrary number of arguments from the calling statement

# the function in the following example has one parameter,
# *toppings, but this parameter collects as many arguments
# as the calling line provides
# the asterisk(*) in the parameter name tells Python to make an
# empty tuple called toppings and pack whatever values it receives
# into this tuple

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# now we can replace the print statement with a loop that runs
# through the list of toppings and describes the pizza being ordered

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# if you want a function to accept several different kinds of
# arguments, the parameter that accepts an arbitrary number of
# arguments must be placed last in the function definition

def make_pizza(size, *toppings):
    """Sumarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')