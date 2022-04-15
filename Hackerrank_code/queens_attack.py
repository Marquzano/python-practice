# we are given the size of a board, n
# we are given the number of obstacles on the board, k
# we are given the coordinates of the queen, r_q and c_q
# we are also given the list of coordinates of the obstacles, obstacles (arr[k][2])
# we are meant to figure out the number of spots the queen can move to

# make an empty board
def makeBoard(n):
    board = {}
    for i in range(n - 1, 0):
        board[i] = [' '] * n
    print(board)
    return board

def prettyPrint(n, board):
    # just print this in descending order?
    for i in range(n):
        print(board[i])

def queensAttack(n, k, r_q, c_q, obstacles):
    board = makeBoard(n)
    # this populates the board with obstacles
    for i in range(k):
        pos = obstacles[i]
        pos_x = pos[0] - 1
        pos_y = pos[1] - 1
        board[pos_x][pos_y] = 'x'
    # this places the queen on the board
    board[r_q - 1][c_q - 1] = 'q'

    # the dictionary needs to be made so that
    # the rows need to be numbered from bottom to top 1 - n
    # the columns need to be numbered from left to right 1 - n
    # in the case of the dictionary it will be 0 - n-1
    # does it really matter that the board I have has rows
    # numbered from top to bottom 0 - n-1?
    # more on this later

    prettyPrint(n, board)

queensAttack(5, 2, 3, 2, [[2,5],[4,3]])