#This script introduces python's range function

#This will output up to 4
for value in range(1,5):
    print(value)
print('\n')

#If you want to include the number 5 then increase your range by one
for value in range(1,6):
    print(value)
print('\n')

#You can also use the range function as well as the list wrapper function to create a list
numbers = list(range(1,6))
print(numbers)