#Demonstrating the use case of conditional statements when verifying usernames for a website

current_users = ['marquzano', 'angelm', 'jeorgia.lamb', 'mangelica', 'pescadito']

new_users = ['john1234', 'Jeorgia.Lamb', 'angelm', 'sarahS', 'bob4321']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("\n" + new_user + " is taken.\nPlease enter another username")
    else:
        print("\n" + new_user + " is available.")