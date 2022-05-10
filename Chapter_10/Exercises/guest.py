name = input("Please let us know your name: ")

filename = '../text_files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name.title() + "\n")