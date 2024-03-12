# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

# here is my partial solution
# need to continue working on zigzag logic
# review and then continue from line 56
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # create list of lists
        rows = []
        zigZag = ''
        # where the length of the outer list is numRows
        # and the inner lists are made up of the characters in s

        # need to populate rows
        i = 0
        j = 0
        while i < numRows:
            rows.append([])
            i += 1
        
        s = list(s)
        # this process is not zigzagging
        # more like straightlining?
        while s:
            if j > (len(rows) - 1):
                j -= 1
            elif j < 0:
                j += 1
            rows[j].append(s.pop(0))
            # needs to be a switch mechanism here
            # to increment j and decrement j when needed
        # debugging
        # for row in rows:
        #     print(row)

        # join character of each row to one another

        # return zigzag conversion