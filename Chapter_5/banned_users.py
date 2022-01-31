#Here we will be using the in keyword to check if a value is NOT in the list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')