#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

# Staircase detail

# This is a staircase of size n = 4:

#    #
#   ##
#  ###
# ####
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

# Function Description

# Complete the staircase function in the editor below.

# staircase has the following parameter(s):

# int n: an integer
# Print

# Print a staircase as described above.

# Input Format

# A single integer, n, denoting the size of the staircase.

# Constraints

#  0 < n <= 100.

# Output Format

# Print a staircase of size n using # symbols and spaces.

# Note: The last line must have 0 spaces in it.

# Sample Input

# 6 
# Sample Output

#      #
#     ##
#    ###
#   ####
#  #####
# ######

practiceN = 4

def staircase(n):
    # Write your code here
    staircase = ""
    hashtags = ""
    for i in range(n):
        hashtags += "#"
        print("{:>int(n)}".format(hashtags)) # This line cuases a formatting issue
        
staircase(practiceN)

# if __name__ == '__main__':
#     n = int(input().strip())

#     staircase(n)
