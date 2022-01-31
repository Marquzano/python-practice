#Script meant to demonstrate my understanding of conditional statements

team = 'predators'
print("Is team == 'predators'? I predict True.")
print(team == 'predators')

print("\nIs p in the predators name? I predict True.")
if 'p' in team:
    print(True)

print("\nIs p and a in the predators name? I predict True.")
if 'p' in team and 'a' in team:
    print(True)

print("\nIs o or l in the predators name? I predict True.")
if 'o' in team or 'l' in team:
    print(True)

print("\nIs p or l not in the predators name? I predict True")
if 'p' not in team or 'l' not in team:
    print(True)

guess = "PREDATORS"
print("\nIs PREDATORS the same as predators? I predict True.")
if guess.lower() == team:
    print(True)

age = 24
print("\nIs age greater than 21? I predict True.")
if age > 21:
    print(True)

print("\nIs age greater than or equal to 24? I predict True.")
if age >= 24:
    print(True)

#******************************************************************

print("\nIs team == 'blackhawks'? I predict False.")
print(team == 'blackhawks')

#This returns false since the values are case sensitive in Python
print("\nIs P in the predators name? I predict False.")
if 'P' in team:
    print("Surprisingly yes??")
else:
    print(False)

print("\nIs b and h in the predators name? I predict False.")
if 'b' in team and 'h' in team:
    print("Surprisingly yes???")
else:
    print(False)

print("\nIs w or l in the predators name? I predict False.")
if 'w' in team or 'l' in team:
    print("I guess so???")
else:
    print(False)

print("\nIs p or e not in the predators name? I predict False")
if 'p' not in team or 'e' not in team:
    print("Whaaat??")
else:
    print(False)

guess = "BLACKHAWKS"
print("\nIs BLACKHAWKS the same as predators? I predict False.")
if guess.lower() == team:
    print("This is awfully surprising?")
else:
    print(False)

print("\nIs age less than 21? I predict False.")
if age < 21:
    print("This is unsettling.")
else:
    print(False)

print("\nIs age less than or equal to 23? I predict False.")
if age <= 23:
    print("This is also unsettling.")
else:
    print(False)