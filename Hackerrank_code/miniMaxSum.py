# This code is meant to be a solution for the miniMaxSum problem
# essentially we are given an array of 5 integers
# we are then to find the minimum and maximum summations of 4 of the 5 integers
# once we find them we must print them out in a single line separated by a space

def miniMaxSum(arr):
    maxSum = 0
    minSum = 0
    maxInt = max(arr)
    minInt = min(arr)

    arr.remove(maxInt)
    for i in range(len(arr)):
        minSum += arr[i]

    arr.append(maxInt)
    arr.remove(minInt)
    for i in range(len(arr)):
        maxSum += arr[i]

    print(str(minSum) + " " + str(maxSum))

miniMaxSum([10,4,7,4,5])