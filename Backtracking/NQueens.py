n = 4
board = [["."] * n for _ in range(n)]
result = []

rowSet = set()
colSet = set()
diagonal = set() # i - j
antiDiagonal = set() # i + j

def dfs(col):
    #bc
    if col == n:
        for row in board:
            print(row)
        print()
        # newAns = []
        # for row in board:
        #     newAns.append(row[::])
        # result.append(board[::])
        return
    for row in range(n):
        if row in rowSet or col in colSet:
            continue
        if (row - col) in diagonal:
            continue
        if (row + col) in antiDiagonal:
            continue
        
        board[row][col] = 'Q'
        rowSet.add(row)
        colSet.add(col)
        diagonal.add(row - col)
        antiDiagonal.add(row + col)
        dfs(col + 1)

        board[row][col] = '.'
        rowSet.remove(row)
        colSet.remove(col)
        diagonal.remove(row - col)
        antiDiagonal.remove(row + col)


dfs(0)
print(result)


