#This script introduces tuples

dimensions = (200, 5) #Tuples are defined using parentheses instead of square brackets
print(dimensions[0])
print(dimensions[1])

#Lets see what happens when we try to change an item in the tuple
# dimensions[0] = 250 #It creates an error becuase tuples do not allow item assignment

#You can loop through tuples same as with lists
for dimension in dimensions:
    print(dimension)
print("\n")

#Tuples do not support item assignment but we can define the variable with a new tuple altogether
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Tuples are simple data structures. Use them to store values that should not be changed