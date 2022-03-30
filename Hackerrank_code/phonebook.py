# Enter your code here. Read input from STDIN. Print output to STDOUT
def entry(n):
    phonebook = {}
    for i in range(n):
        name, number = input().split(' ')
        phonebook.update({name: number})
    return phonebook

def search(names):
    for name in names:
        if name not in phonebook:
            print("Not Found")
        else:
            number = phonebook.get(name)
            print(name + "=" + number)
        
if __name__ == '__main__':
    n = int(input())
    
    phonebook = entry(n)
    
    names = []
    # need to figure out how to get a continuous stream of input
    # then I need to determine when to stop trying to get input
    # and send it to the function
    names = input().split(" ")
    search(names)