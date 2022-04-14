# this script is to improve the formatting for aliens.py

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for i in range(5):
    for alien in aliens[:5+(3*i)]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

print("What's currently on the field:")

for alien in aliens[:20]:
    print(alien)

greens = 0
yellows = 0
reds = 0
totalPoints = 0
# I want say how many aliens of each color there are on the field
for alien in aliens[:20]:
    if alien['color'] == 'green':
        greens += 1
        totalPoints += alien['points']
    if alien['color'] == 'yellow':
        yellows += 1
        totalPoints += alien['points']
    if alien['color'] == 'red':
        reds += 1
        totalPoints += alien['points']

print("Red aliens: " + str(reds) + "\nYellow aliens: " + str(yellows) + 
    "\nGreen aliens: " + str(greens) + "\nTotal points available: " + str(totalPoints))