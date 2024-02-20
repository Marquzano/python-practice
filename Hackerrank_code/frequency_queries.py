# You are given  queries. Each query is of the form two integers described below:
# - 1 x : Insert x in your data structure.
# - 2 y : Delete one occurence of y from your data structure, if present.
# - 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

# Example
# queries = [[1,1][2,2][3,2][1,1][1,1][2,1][3,2]]
# The results of each operation are:
# Operation     Array       Output
# (1,1)         [1]
# (2,2)         [1] 
# (3,2)         [1]         0
# (1,1)         [1,1]
# (1,1)         [1,1,1]
# (2,1)         [1,1]
# (3,2)         [1,1]       1
# Return an array with the output: [0,1].

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
# this solution has a very high time complexity so it was not able to pass
# testing and optimizing here in VS Code
def freqQuery(queries):
    # create the 2D hashmap of the queries
    resultantArr = []
    i = 0
    output = []
    while i < len(queries):
        # here we go through each operation
        # given in queries
        if queries[i][0] == 1:
            resultantArr.append(queries[i][1])
        if queries[i][0] == 2:
            try:
                resultantArr.pop(queries[i][1])
            except:
                continue
        if queries[i][0] == 3:
            # how do we keep count of the number
            # of instances for each value?
            # we could use a dictionary
            # the key could be the value
            # the value would be the number of instances of the 'value' which is
            # the key
            numberOfInstances = {}
            manResultantArr = resultantArr
            while manResultantArr:
                if manResultantArr[0] in numberOfInstances.keys():
                    numberOfInstances[manResultantArr[0]] += 1
                    manResultantArr.pop(0)
                else:
                    numberOfInstances[manResultantArr[0]] = 1
                    manResultantArr.pop(0)
            
            if queries[i][1] in numberOfInstances.values():
                output.append(1)
            else:
                output.append(0)
    return output
            
# hardcoded sample queries
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    queries = [[1,1],[2,2],[3,2],[1,1],[1,1],[2,1],[3,2]]

    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
