phonebook = {}
    
# this function adds n entries of names and corresponding phone numbers
def entry(n):
    for i in range(n):
        name, number = input().split(' ')
        phonebook.update({name: number})

entry(3)

print(phonebook)

# this function searches the number of names given
# it gives the key value pair
# if the name is not in the phonebook then it returns Not Found
def search(n):
    for i in range(n):
        name = input()
        if name not in phonebook:
            print("Not Found")
        else:
            number = phonebook.get(name)
            print(name + "=" + number)

search(4)        