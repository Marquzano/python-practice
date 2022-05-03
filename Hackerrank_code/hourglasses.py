# I want to make a dictionary where the keys are indexed from 1 - 16
# the values will be a list of the numbers that make up the hour glasses in the array A
# this way we can traverse the hourglasses and populate the dictionary
# afterwards we can calculate the sums of each hourglass and put them in a list where
# we can finally find the max possible sum of the given hourglasses

def traverseHourglasses(hourglasses, arr):
    """Retrieves all of the values in an hourglass for each hourglass"""
    # we can make a splice of each row of length 3 like such [j:j+2]
    # this has to increment from 0 to 3 and then reset when we move a row
    # if j = 3 i += 1 this moves the row
    # once i > 3 we are done collecting the values for each of the 'tops'
    i, j = 0, 0
    for k in range(16):
        if j > 3:
            j = 0
            i += 1
        hourglasses[k] = []
        tops = arr[i][j:j+3]
        for num in tops:
            hourglasses[k].append(num)
        j += 1
    i, j = 2, 0
    for k in range(16):
        if j > 3:
            j = 0
            i += 1
        bots = arr[i][j:j+3]
        for num in bots:
            hourglasses[k].append(num)
        j += 1
    i, j = 1, 1
    for k in range(16):
        if j > 4:
            j = 1
            i += 1
        mid = arr[i][j]
        hourglasses[k].append(mid)
        j += 1

def findMaxSum(hourglasses):
    """Gives the max sum possible from the given hourglasses"""
    sums = []
    for values in hourglasses.values():
        summation = sum(values)
        sums.append(summation)
    return max(sums)


if __name__ == '__main__':
    # hourglasses will hold the list of values in each hourglass in the array
    hourglasses = {}
    arr = []

    # expecting result = 19 with the given array
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    traverseHourglasses(hourglasses, arr)
    result = findMaxSum(hourglasses)
    print(result)