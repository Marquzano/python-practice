# now that we know about while loops we can make parrot.py
# run continuously until the user is done

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    # if message == 'quit':
    #     print("You quit")
    # else:
    #     print(message)
    if message != 'quit':
        print(message)