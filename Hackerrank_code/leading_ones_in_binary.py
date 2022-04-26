#!/bin/python3

import math
import os
import random
import re
import sys

def leadingOnes(binary):
    """this will return the max number of leading ones in a binary number"""
    # will continue on this challenge at a later time

def convertToBinary(n):
    """Takes a base 10 integer and returns base 2 binary representation"""
    binaryArr = []
    bit = 0
    while n != 0:
        bit = n % 2
        n = n//2
        binaryArr.append(bit)
    binaryArr = binaryArr[::-1] # have to reverse the order
    return binaryArr


if __name__ == '__main__':
    n = int(input().strip())

    binaryN = convertToBinary(n)

    # print(str(binaryN))

    result = leadingOnes(binaryN)