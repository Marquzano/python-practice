# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# my code so far
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # in this problem we need only detect if 
        # the board is valid to begin with
        # we have to check if each row has any repeating numbers
        # we have to check if each column has any repeating numbers
        # we have to check in  each box if there are any repeating numbers
        
        # would be better if rows were represented as a dictionary and not list[list[]]
        # would change complexity of below from n^3 to n^2
        # check rows first
        for row in board:
            i = 0
            j = 1
            for i in range(len(row) - 1):
                for j in range(i + 1, len(row)):
                    # these prints are for debugging
                    print("Current Row: " + str(board.index(row)))
                    print("First number: " + row[i] + "\nSecond number: " + row[j]
                            + "\nIndex of first: " + str(i) + "\nIndex of second: " + str(j))
                    print('\n')
                    if row[i] == row[j] and (row[i] != '.' and row[j] != '.'):
                        # how are both examples getting here?
                        # need to debug here
                        return False
                    j += 1
                i += 1
        
        # define dictionary called columns
        # the values will be the columns of the board
        # from 0 - 8 L -> R
        columns = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        i = 0
        for row in board:
            for value in columns.values():
                value.append(row[i])
                i += 1
            i = 0
        
        # need to check columns now that we have it here

        # still need to come up with logic to check boxes