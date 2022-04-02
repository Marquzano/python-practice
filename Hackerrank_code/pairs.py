# what I have so far for the pairs problem

def pairs(k, arr):
    # make a pairs variable
    pairs = 0
    # begin by subtracting each possible pair
    print(arr)
    # I may need to do this with indexes to keep it correct
    for first in arr:
        print("First(before difference for loop): " + str(first))
        for second in arr[1:]:
            print("Second: " + str(second))
            diff = abs(first - second)
            if diff == k:
                pairs += 1
        print("First(after difference for loop): " + str(first))
        # arr.remove(first)
    return pairs

k = 2
arr = [1,5,3,4,2]

print(pairs(k, arr))