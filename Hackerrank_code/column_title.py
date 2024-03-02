# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 
# Example 1:
# Input: columnNumber = 1
# Output: "A"


# solution is still not complete
# give extra test cases to debug
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # there are 26 letters in the alphabet
        # if we are given anything less than 26
        # we return the single letter
        # if it is greater than 26 we will have to divide it by 26 
        # everytime we divide by 26 is another Z that needs to be appended
        # whatever quotient remains comes after the leading Zs (if any) is appended
        # the remainder then also gets appended as the last letter in the column name 

        letterDictionary = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J',
                            11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S',
                            20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

        columnTitle = []
        lastRemainder = 0

        if columnNumber < 27:
            return letterDictionary[columnNumber]
        else:
            # here we handle columns that are greater than Z
            remaining = columnNumber/26
            while floor(remaining) > 26:
                columnTitle.append('Z')
                remaining /= 26
                lastRemainder = remaining % 26
            columnTitle.append(letterDictionary[floor(remaining)])
            columnTitle.append(letterDictionary[floor(lastRemainder)])
            return str(columnTitle)