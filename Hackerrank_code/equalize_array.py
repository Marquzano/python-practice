def equalizeArray(arr):
    # Write your code here
    # figure out the value with most repititions in the array
    # if there are two values with the same amount of repititions
    # choose the first one
    # most will house the index 
    diffArr = arr[:]
    values = {}
    uniqueValues = set(arr)
    for uniqueValue in uniqueValues:
        numOfValue = 0
        while uniqueValue in diffArr:
            numOfValue += 1
            diffArr.remove(uniqueValue)
        values[numOfValue] = uniqueValue
    most = max(values.keys())
    return abs(most - len(arr))

sampleArr = [1, 3, 3, 4, 5, 5]

result = equalizeArray(sampleArr)
print(result)