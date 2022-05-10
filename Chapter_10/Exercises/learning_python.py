filename = '../text_files/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.read()
    print(lines)
    print(lines)
    print(lines)
print("\n")

with open(filename) as file_object:
    lines = file_object.read()
    print(lines)
print("\n")

with open(filename) as file_object:
    for line in file_object:
        print(line)
print("\n")

with open(filename) as file_object:
    lines = ''
    for line in file_object:
        lines += line

print(lines)