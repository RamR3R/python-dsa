def move(i , j , path , maze , result , visited):
    # base condition:
    # print( i , j , path , visited)
    if i == len(maze) or  j == len(maze[i]) or i == -1 or j == -1:
        return
    if visited[i][j] == True:
        return
    if maze[i][j] == 0:
        return
    if i == len(maze) - 1 and j == len(maze[i]) - 1:
        result.append(path)
        return

    #recursive calls
    visited[i][j] = True
    move(i + 1 , j , path + "D" , maze , result , visited)
    #backtrack and remove the R
    move(i , j + 1 , path + "R" , maze, result , visited)
    # move towards L
    move(i , j - 1 , path + "L" , maze , result , visited)
    # move my rat to up
    move(i - 1 , j , path + "U" , maze , result , visited)
    visited[i][j] = False # backtracking



question = [
            [1 , 1 , 1 , 1],
            [1 , 0 , 0 , 1],
            [1 , 1 , 1 , 1],
            [1 , 1 , 0 , 1]
        ]
n = len(question)
visited = [[False] *n for i in range(0, n)]
result = []
move(0, 0 , "" , question , result , visited)
print(result)