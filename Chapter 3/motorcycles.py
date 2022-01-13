#This script provides the basics of list manipulability

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#How to modfy the elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#How to append items to a list
motorcycles.append('honda')
print(motorcycles)
print('\n')

#You can append to an empty list
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print('\n')

#You can insert elements into a list by providing its index and value with the insert method
motorcycles.insert(0, 'ducati')
print(motorcycles)
print('\n')

#You can remove an item from a list using its index
#This will delete the value permanently so be careful
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
print('\n')

#You can remove an item from a list and use that value with the pop method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print('\n')

#Example use case
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print('\n')

#You can pop any item from the list if you provide the index
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print('\n')

#You can remove an element by using its value
#If there are duplicates of the value in the list the remove method will remove the first appearance of the value in the list
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
print('\n')

#You can use the value when using the remove method as so in the following use case
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')