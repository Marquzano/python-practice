vacation_spots = {}

active = True

while active:
    vacation_spot = input("\nIf you could visit one place in the world where would you go? ")
    name = input("Please tell us your name: ")

    vacation_spots[name] = vacation_spot

    keep_going = input("Is there still another person who must take the poll?(yes/no): ").strip()
    if keep_going.lower() == 'no' or 'no' in keep_going.lower():
        active = False

for name, vacation_spot in vacation_spots.items():
    print("\n" + name.title() + " would love to take a vacation in " + vacation_spot.title() + " one day.")