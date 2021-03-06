#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# this is an example of a recursive function
def factorial(n):
    # base case
    if n == 1:
        return n
    # recursive case
    else:
        return (n * factorial(n-1))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = factorial(n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()