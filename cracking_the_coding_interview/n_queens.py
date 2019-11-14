'''
N-Queens problem from hackerearth.com
A problem for studying recursion and backtracking

Given a chess board having  cells, we need to place
queens in such a way that no queen is attacked by
any other queen. A queen can attack horizontally,
vertically and diagonally.
'''
def is_attacked(x, y, board, N):
    # check for x row or y column
    for i in range(N):
        if board[x][i] == 1 or board[i][y] == 1:
            return True
    # check for diagonals
    for p in range(N):
        for q in range(N):
            if (p + q) == (x + y) or  (p - q) == (x - y):
                if board[p][q] == 1:
                    return True
    return False
def N_queens(board, n, N):
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 or is_attacked(i, j, board, N):
                continue
            board[i][j] = 1
            if N_queens(board, n - 1, N):
                return True
            board[i][j] = 0
    return False
# Test Case
N = int(raw_input())
output = "NO"
board = [[0]*N for i in range(N)]

if N_queens(board, N, N):
    output = "YES"
    print output
    for i in range(N):
        row = ""
        for j in range(N):
            row += str(board[i][j]) + " "
        print row[:-1]
else:
    print output
