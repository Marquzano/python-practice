#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

# what I have so far
# need to figure out why extra letters are not being removed in the for loops
def makeAnagram(a, b):
    # Write your code here
    count = 0
    i = 0
    j = 0
    # make both strings into lists
    # determine first what characters from list a are in list b
    # delete them from a and keep count
    listA = list(a)
    listB = list(b)
    print("Before any deletion")
    print("ListA: " + str(listA))
    print("ListB: " + str(listB))
    print("Count: " + str(count))
    for i in range(len(listA) - 1):
        if listA[i] not in listB:
            listA.remove(listA[i])
            count += 1
        i += 1
    print("After ListA deletion")
    print("ListA: " + str(listA))
    print("ListB: " + str(listB))
    print("Count: " + str(count))
    for j in range(len(listB) - 1):
        if listB[j] not in listA:
            listB.remove(listB[j])
            count += 1
        j += 1
    print("After ListB deletion")
    print("ListA: " + str(listA))
    print("ListB: " + str(listB))
    print("Count: " + str(count))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
