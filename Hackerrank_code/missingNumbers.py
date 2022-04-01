# the code for missingNumbers problem

def missingNumbers(arr, brr):
    # make an array for missingInts
    missingInts = []
    # remove values from brr
    # that are in arr
    for i in range(len(arr)):
        if arr[i] in brr:
            brr.remove(arr[i])
    # handle the duplicates that remain in brr
    for number in brr:
        # append numbers that aren't already in missingInts
        if number in missingInts:
            continue
        else:
            missingInts.append(number)
    # sort the list
    missingInts.sort()
    return missingInts

arr = [205, 205, 206, 207, 210, 210]
brr = [205, 205, 206, 206, 207, 210, 210, 210, 211, 211]
# in this case we expect the array to be:
# [206, 210, 211]
result = missingNumbers(arr, brr)

print(result)