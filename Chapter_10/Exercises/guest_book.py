filename = '../text_files/guest_book.txt'

with open(filename, 'w') as file_object:
    file_object.write("This is a guest book of all" +
                    " who execute this program.\n")

while True:
    print("Please tell us your name:")
    name = input("(to exit enter 'exit') ")
    if 'exit' in name.lower():
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name.title() + "\n")