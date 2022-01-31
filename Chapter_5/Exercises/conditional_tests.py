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