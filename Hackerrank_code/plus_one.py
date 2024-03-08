# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# this is the complete solution
# could very well be optimized
# currently I believe it is O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # holds the result
        result = []

        # turn into a string
        strInt = ''
        for digit in digits:
            strInt += str(digit)

        # turn the string into an int
        number =  int(strInt)

        # increment by 1
        number += 1
        
        # turn result into string
        strNumber = str(number)
        
        # turn string into list
        numsStr = list(strNumber)
        
        # typecast each value as an int
        for num in numsStr:
            # append it to the result array
            result.append(int(num))

        return result