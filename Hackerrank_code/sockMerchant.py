# this challenge requires us to take
# input n, the number of socks in a pile,
# and input arr[n], which is the array of colors
# we must return the number of pairs as an int

# the solution I am attempting to implement here is to
# take the array of socks and get the unique colors
# this set will then be the keys to a dictionary
# the values for the keys will be the number of socks that
# are that color in the array

def sockMerchant(n, arr):
    # set pairs to 0
    pairs = 0
    # here we get the unique colors of the pile
    uniqueColors = set(arr)
    # make an empty dicitonary to be populated with data
    sortedPile = {}
    # first set the keys in the dictionary
    for i in uniqueColors:
        sortedPile[i] = 0
    # now we sort them out in the dictionary
    for color in sortedPile:
        # here we go through the pile
        for j in range(n):
            # if the color is equal to the color then increment
            if color == arr[j]:
                sortedPile[color] += 1
    # now that we have them sorted out
    # we can look at the sortedPile and determine the number of pairs per color
    for sameColor in sortedPile.values():
        pairs += sameColor // 2
    return pairs

sampleArr = [1,2,1,2,1,3,2]
samplePairs = sockMerchant(len(sampleArr), sampleArr)
print(samplePairs)