#This script introduces slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#This line prints a slice of the list above
print(players[0:3])

#If you wanted to print the second third and fourth items in a list you would do the following
print(players[1:4])

#If you were to omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])

#It works similarly if you omitted the second index, this time the slice begins with the first index and continues until the last item in the list
print(players[2:])

#Remember that a negative index returns an element a certain distance from the end of a list
#This also works with the slice, for example if we want the last three items from a list we could do the following
print(players[-3:])

#We can use slices in a for loop if we wanted to work with a subset of the elements in a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())