# what I have so far for the pairs problem
# ok so I believe we could still iterate through the original array
# it's the array we iterate over in the second for loop that needs to change


def pairs(k, arr):
    # make a pairs variable
    pairs = 0
    # begin by subtracting each possible pair
    for i in range(len(arr)):
        diffArr = arr[i+1:]
        for j in range(len(diffArr)):
            diff = abs(arr[i] - diffArr[j])
            if diff == k:
                pairs += 1
    return pairs

k = 3
arr = [1,5,3,4,2]

print(pairs(k, arr))

# reference code from below to come up with an idea
# for adjusting the size of the comparison array
# according to the index of the first array
# I will need to adjust the loops from above to work through an index
# Bonus Note is that it was suggested that you could compare with greater ease using dictionaries
# google coding interview

# pair = False
# numDiff = 0
# for i in range(len(arr)):
#   # second for loop is to compare
#   comparisonArr = arr[i+1:]
#   for j in range(len(comparisonArr)):
#     firstStr = arr[i]
#     secondStr = comparisonArr[j]
#     # another for loop to compare each character in the string
#     for i in range(m):
#       if firstStr[i] == secondStr[i]
#         continue
#       elif firstStr[i] != secondStr[i]
#         numDiff += 1

#     if numDiff == 1:
#       pair = True
#       return pair
#     else:
#       pair = False
#     numDiff = 0