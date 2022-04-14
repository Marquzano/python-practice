# the input() function takes one argument: the prompt, or instructions,
# that we want to dipslay to the user so they know what to do

message = input("Tell me something, and I will repeat it back to you: ")
if "i'm an idiot" in message.lower() or "im an idiot" in message.lower():
    print("You're an idiot!") # lol
else:
    print(message)