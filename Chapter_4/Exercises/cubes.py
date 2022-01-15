#This script prints out the cubes of the first ten numbers

cubes = []

for number in range(1,11):
    cubes.append(number**3)

for cube in cubes:
    print(cube)