# in Chapter 3 we used remove() to remove a specific value from a list
# the remove() function worked because the value we were interested in
# appeared only once in the list. But if you want to remove all instances
# of a value from a list?

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)