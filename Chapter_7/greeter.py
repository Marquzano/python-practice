# this is here so that we do not need to constantly
# give input when we are checking new code and we 
# can keep track of where we're at in the file
def uncommentCodeMessage(number):
    uncommentMessage = "Uncomment code " + str(number) + " to run it"
    print(uncommentMessage)

# make sure to write clear prompts that tell the user exactly
# what kind of information you are looking for

uncommentCodeMessage(1) 
print("\n")
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# sometime's you'll want to write prompt that's longer than one line
# i.e. you might want to tell the user why you're asking for a certain input

uncommentCodeMessage(2)
print("\n")
# prompt = "If you tell us who you are, we can personalize the messages you see"
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("Hello, " + name + "!")

# when you use the input() function, Python interprets everything the user enters as a string

# uncommentCodeMessage(3)
# print("\n")
