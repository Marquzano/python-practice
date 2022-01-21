#This script shows my comprehension of copying and manipulating lists
pizzas = ['vegan larry tate', 'earth mother', 'v for vegan']

friend_pizzas = pizzas[:]

pizzas.insert(0, 'vegan bianca')

friend_pizzas.append('pepperoni')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('\n')

print('My friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)