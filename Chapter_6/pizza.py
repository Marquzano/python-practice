# rather than putting a dictionary inside a list, it's sometimes
# useful to put a list inside of a dictionary

# store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)