#This script showcases my understanding of slices in for loops
my_foods = ['pizza', 'falafel', 'carrot cake', 'burger', 'pad thai', 'pasta']

print('The first three items in the list are:')
for food in my_foods[:3]:
    print(food)

print('Three items from the middle of the list are:')
for food in my_foods[1:-2]:
    print(food)

print('The last three items in the list are:')
for food in my_foods[-3:]:
    print(food)