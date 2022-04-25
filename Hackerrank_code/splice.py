

def splice(n, words):
    # go through them in a for loop
    evens, odds = '', ''
    for i in range(n):
        word = words[i]
        for j in range(len(word)):
            if j % 2 == 0:
                evens += word[j]
            else:
                odds += word[j]
        print(evens + " " + odds)
        evens, odds = '', ''
            

if __name__ == '__main__':
    # take the input 
    prompt = "Please give the number of words to splice then enter those words one at a time:"
    prompt += "\nEnter a blank string to indicate when you are done. "
    num = int(input(prompt))
    words = []
    
    while True:
        word = input()
        if word != '':
            words.append(word)
        else:
            break
        
    splice(num, words)

    # this will be for the hackerrank compiler
    # while True:
    #     try:
    #         word = input()
    #         words.append(word)
    #     except:
    #         break