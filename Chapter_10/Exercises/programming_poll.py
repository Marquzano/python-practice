filename = '../text_files/programming_poll.txt'

while True:
    print("Please tell us your favorite part about programming:")
    message = input("(to exit enter 'exit') ")
    if 'exit' in message.lower():
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(message + "\n")