#!/bin/python3

import math
import os
import random
import re
import sys

def leadingOnes(binary):
    """This will return the max number of leading ones in a binary number"""
    # the variable count is supposed to keep up with consecutive ones in the binary sequence
    # countArr is to append each count of consecutive ones in the sequence
    count = 0
    countArr = []
    for i in range(len(binary)):
        # here we increase the count for every consecutive one in the sequence
        if binary[i] == 1:
            count += 1
            # this nested if is to help append the remaining count when we reach the end
            # and can't append in the other cases
            if i + 1 == len(binary) and binary[i] == 1:
                countArr.append(count)
        # once we encounter a zero we append the last count of consecutive ones
        # then we reset the count
        else:
            countArr.append(count)
            count = 0
        # if the entire sequence is consecutive ones we append the count as such to the count array
        if count == len(binary):
            countArr.append(count)
    return max(countArr)

def convertToBinary(n):
    """Takes a base 10 integer and returns base 2 binary representation"""
    binaryArr = []
    bit = 0
    while n != 0:
        bit = n % 2
        n = n//2
        binaryArr.append(bit)
    binaryArr = binaryArr[::-1] # have to reverse the order to be a proper binary sequence
    return binaryArr


if __name__ == '__main__':
    while True:
        print("Please enter a number:")
        n = input("(If you are done enter 'q' to quit) ").strip()
        if n == 'q' or 'q' in n.lower():
            break
        n = int(n)

        binaryN = convertToBinary(n)

        print(str(binaryN))

        result = leadingOnes(binaryN)
        print(result)