destinations = ['spain', 'germany', 'austria', 'finland', 'japan']

#Print as is
print(destinations)
#Print sorted list without permanently changing the order
print(sorted(destinations))
#Print the original
print(destinations)
#Print in reverse order without permanently changing the list
print(sorted(destinations, reverse = True))
#Print the original
print(destinations)
#Permanently reverse the order of the list
destinations.reverse()
print(destinations)
#Reverse it once more to show it in its original order
destinations.reverse()
print(destinations)
#Sort the list in alphabetical order permanently
destinations.sort()
print(destinations)
#Sort the list in reverse alphabetical order permanently
destinations.reverse()
print(destinations)