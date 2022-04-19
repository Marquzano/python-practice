
# use a conditional test in the while statement to stop the loop
prompt = "How old are you? "
age = ''
while age == '':
    age = int(input(prompt))
    if age < 3:
        print("The ticket is free")
    elif 3 <= age <= 12:
        print("The ticket is $10")
    elif age > 12:
        print("The ticket is $15")

# use an active variable to control how long the loop runs
prompt = "How old are you? "
active = True
while active:
    age = int(input(prompt))
    if age < 3:
        print("The ticket is free")
        active = False
    elif 3 <= age <= 12:
        print("The ticket is $10")
        active = False
    elif age > 12:
        print("The ticket is $15")
        active = False

# use a break statement to exit the loop when the user enters a 'quit' value
prompt = "How old are you?"
prompt += "\n(Enter 'quit' after you've entered your age) "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("The ticket is free")
    elif 3 <= int(age) <= 12:
        print("The ticket is $10")
    elif int(age) > 12:
        print("The ticket is $15")