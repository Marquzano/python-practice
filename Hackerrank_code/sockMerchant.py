# this challenge requires us to take
# input n, the number of socks in a pile,
# and input arr[n], wich is the array of colors
# we must return the number of pairs as an int

def arrayToDict(arr):
    sampleDict = {}
    for i in range(len(arr)):
        sampleDict.update({i+1: arr[i]})
    return sampleDict

def flip(dict):
    flipped = {}
    for key, value in dict.items():
        if value not in dict:
            flipped[value] = [key]
        else:
            flipped[value].append(key) # this line is giving me KeyError: 1
    return flipped

def sockMerchant(n, arr):
    pairs = 0
    sockDict = arrayToDict(arr)
    flippedSockDict = flip(sockDict)
    return flippedSockDict

sampleArr = [1,2,1,2,1,3,2]

print("sampleArray: ", str(sampleArr))
print("Dictionary of sampleArray: ", str(arrayToDict(sampleArr)))
print("The flipped version of the dictionary: ", str(sockMerchant(7, sampleArr)))