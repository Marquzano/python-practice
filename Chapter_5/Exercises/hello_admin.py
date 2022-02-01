#Simple script using if statements and lists with a for loop

users = ['admin', 'angel', 'jeorgia', 'arvi', 'cash']
# users = [] #A sample case to show how we handle empty lists

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        elif user == 'angel' or user == 'jeorgia':
            print("Hello " + user.title() + ", thank you for logging in again!")
        else:
            print("Woof " + user.title() + ", ruff ruff woof woof!")
else:
    print("We need to find some users!")