#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

practiceArr = [[1, 2, 3, 4], 
               [4, 5, 6, 7], 
               [9, 8, 9, 2],
               [3, 7, 8, 1]]

def diagonalDifference(arr):
    # Write your code here
    lrd = 0
    rld = 0
    n = len(arr)
    # for lrd they are going to be ascending in paired order
    for i in range(n):
        lrd += arr[i][i]
        print(lrd)
    # for rld they are going to be ascending in opposite order
    for i in range(n):
        rld += arr[i][n-1-i]
        print(rld)
    return abs(lrd - rld)

print(diagonalDifference(practiceArr))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
