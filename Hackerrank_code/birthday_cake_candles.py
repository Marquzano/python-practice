# for this problem we are mean to locate the number of "max height" candles on a birthday cake
# after we get the total we must return the value

def birthdayCakeCandles(arr):
    # first identify the max unit
    maxUnit = max(arr)
    numOfMax = 0

    # next identify how many duplicates their are of the max unit
    for i in range(len(arr)):
        if arr[i] == maxUnit:
            numOfMax += 1
        else:
            continue
    
    return numOfMax

candles = [3,2,1,3]
print(str(birthdayCakeCandles(candles)))