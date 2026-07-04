n = 3
m = 3
grid = [
    [0 , 0 , 0],
    [0 , 1 , 0],
    [1 , 0 , 0]
    ]
dp = [[0] * m for _ in range(n)]
# for i in range(n):
#     x = []
#     for j in range(m):
#         x.append(-1)
#     dp.append(x)

def dfs( i , j): # TC => O(n * m) || SC => O(n * m) Memorization
    # if i == 0 or  j == 0:
    #     return 1
    # if grid[i][j] == 1:
    #     dp[i][j] = 0

    # if dp[i][j] != -1:
    #     return dp[i][j]
    
    # dp[i][j] = dfs(i - 1 , j) + dfs( i , j - 1)

    for j in range(n):
        if grid[0][j] == 1:
            break 
        dp[0][j] = 1
    for i in range(n):
        if grid[i][0] == 1:
            break
        dp[i][0] = 1
    print(dp)
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[n-1][m-1]





print(dfs(n-1 , m-1))