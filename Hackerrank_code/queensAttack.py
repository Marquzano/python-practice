# we are given the size of a board, n
# we are given the number of obstacles on the board, k
# we are given the coordinates of the queen, r_q and c_q
# we are also given the list of coordinates of the obstacles, obstacles (arr[k][2])
# we are meant to figure out the number of spots the queen can move to

# make an empty board
def makeBoard(n):
    board = {}
    for i in range(n):
        board[i] = [''] * n
    return board

def queensAttack(n, k, r_q, c_q, obstacles):
    board = makeBoard(n)
    # this populates the board with obstacles
    for i in range(k):
        pos = obstacles[i]
        pos_x = pos[0]
        pos_y = pos[1]
        board[pos_x][pos_y] = 'x'
    # we may need to update the board dictionary to start on count 1 and not 0
    # we did populate the board with the obstacles and queen
    # this places the queen on the board
    board[r_q][c_q] = 'q'
    print(board)

queensAttack(5, 2, 0, 0, [[1,2],[3,1]])