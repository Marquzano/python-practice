#An introduction to sorting lists using the sort method
#You cannot revert to the original order after calling this method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Introducing the sorted method
#This temporarily sorts your list but doesn't affect the actual order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#This is how we reverse the order
#The list is changed permanently but can be reverted by calling the method a second time on the list
print('\n')
print(cars)

cars.reverse()
print(cars)