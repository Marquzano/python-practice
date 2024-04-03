# Given a string expression of numbers and operators, return all possible results 
# from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
# The test cases are generated such that the output values fit in a 32-bit integer and the number of different 
# results does not exceed 104.

# Example 1:
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2

# Example 2:
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

# what I have so far
# leetcode is using someother character for '-', that may be an issue
# regEx would help with this
class Solution:
    def diffWaysToCompute(self, expression: str):
        # we need to break the expression up between integers and operations
        operations = ['+','-','*']
        for operand in operations:
            integers = " ".join(expression.split(operand))
        print(integers)
        # we also know there will have to be at least one less operation than integer