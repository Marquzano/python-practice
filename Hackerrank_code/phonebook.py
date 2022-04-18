# this code completes the phonebook challenge
def entry(n):
    phonebook = {}
    for i in range(n):
        name, number = input().split(' ')
        phonebook.update({name: number})
    return phonebook

def search(names):
    for name in names:
        if name not in phonebook:
            print("Not found")
        else:
            number = phonebook.get(name)
            print(name + "=" + number)
        
if __name__ == '__main__':
    n = int(input())
    
    phonebook = entry(n)
    names = []
    while True:
        try:
            inp = input()
            names.append(inp)
        except:
            break
    
    search(names)