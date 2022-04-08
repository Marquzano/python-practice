# here I will be writing sample code 
# to figure out how to best convert 
# an array into a dictionary

# attempt 1
# this does not work
# you need to make each element in the array
# a sequence to represent a key value pair
# o.w. line 13 gives you an error
# arr = [1,2,3,4]

# def convertDict(arr):
#     return dict(arr)

# sampleDict = convertDict(arr)

# print("The original array: ", arr)
# print("Then Dictionary: ", str(sampleDict))

# attempt 2
arr = [1,3,3,4]

def convertDict(arr):
    sampleDict = {}
    for i in range(len(arr)):
        sampleDict.update({i+1: arr[i]})
    return sampleDict

sampleDict = convertDict(arr)

print("The original array: ", arr)
print("Then Dictionary: ", str(sampleDict))