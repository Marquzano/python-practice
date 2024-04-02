# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# what I have so far
class Solution:
    def spiralOrder(self, matrix):
        # this handles the special case if there is only one row in
        # the matrix
        if len(matrix) == 0:
            return matrix[0]

        # a spiral will follow the same pattern
        # it will go through the first row to begin
        # it will then go down the last column
        # afterwards it will go through the last row in reverse
        # then go up the first column save for the value that has already been traversed
        # it continues as such until the spiral is complete
        # more problem solving notes written in code practice notes