#This script also prints the cube values of the first ten numbers
#But the list is created using list comprehension

cubes = [value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)