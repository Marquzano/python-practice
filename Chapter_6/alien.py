# this simple dictionary stores information about a particular alien

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print('\n')

# dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')

# it's sometimes convenient, or even necessary, to start with an empty dictionary
# and then add each new item to it

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print('\n')

# to modify a value in a dictionary, give the name of the dictionary with the key
# in square brackets and then the new value you want associated with that key

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print('\n')

# when you no longer need a piece of information that's stored in a dictionary,
# you can use the del statement to completely remove a key-value pair.
# as shown below

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)