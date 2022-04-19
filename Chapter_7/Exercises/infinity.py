
prompt = "\nTell me your name:"
prompt += "\n(Enter quit to get out of the program) "

name = input(prompt)
while True:
    if name == 'quit':
        break
    else:
        print("Hello " + name.title() + "!")

# this is an infinite loop even though we offered a way of breaking the loop
# it is not possible since the input is not within the loop to 'quit'