import math
import os
import random
import re
import sys

# I want to make a dictionary where the keys are indexed from 1 - 16
# the values will be a list of the numbers that make up the hour glasses in the array A
# this way we can traverse the hourglasses and populate the dictionary
# afterwards we can calculate the sums of each hourglass and put them in a list where
# we can finally find the max possible sum of the given hourglasses

def traverseHourglasses(hourglasses, arr):
    # what we could do is get the "tops" of the hourglasses first
    # then the "mids" and then finally the "bots"
    # get tops
    for row in arr[:4]:
        print(row)


# def findMaxSum(hourglasses):


if __name__ == '__main__':
    # hourglasses will hold the list of values in each hourglass in the array
    hourglasses = {}
    arr = []

    # for hackerrank
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    # would it be a good idea to send a copy?
    # diffArr = arr[:]
    # print(diffArr)

    traverseHourglasses(hourglasses, arr)