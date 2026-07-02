from collections import deque
grid = [
    [2, 1, 1] ,
    [1, 0, 0] ,
    [0, 0, 1]
    ]

q = deque()
rows = len(grid)
col = len(grid[0])
time = 0
for i in range( 0 , rows): # TC => O(N * N)
    for j in range(0 , col):
        if grid[i][j] == 2:
            q.append((i , j , 0))

while len(q) > 0: # TC => O(4 * N * N)
    x = q.popleft()
    time = x[2]
    adjPoints = [(x[0] - 1 , x[1] , x[2] +1) , #up
                (x[0] + 1 , x[1] , x[2] +1) , # down
                (x[0] , x[1] - 1 , x[2] +1) , # left
                (x[0] , x[1] + 1 , x[2] +1) # right
                ]
    
    for neighbour in adjPoints:
            nr , nc , nt =  neighbour
            if nr < rows and nr >= 0 and nc < col and nc >= 0 and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                q.append((nr , nc , nt))


for i in range( 0 , rows):
    for j in range( 0 , col):
        if grid[i][j] == 1:
             time = -1    
          


print(time)


#push to git please remember!!!!!!!!!!!!!!-