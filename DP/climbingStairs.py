arr = [ 0 , 10, 25 , 10 , 0]
dp = [-1] * 5
dp[0] = 0
def fun(n): #TC = > O(n) || SC => O(n)
    # if n <=1:
    #     return arr[n]
    # if dp[n] == -1:
    #     dp[n] = arr[n] + min(fun(n-2) , fun(n-1))
    
    # dp[0] = arr[0]
    # dp[1] = arr[1]
    # for i in range(2 , n + 1): #TC => O(n) || Sc => O(n)
    #     dp[i] = arr[i] + min(dp[i - 1] , dp[i-2])
    # return dp[n]

    first = arr[0]
    second = arr[1]
    for i in range(2 , n + 1): #TC => O(n) || Sc => O(1)
        third = arr[i] + min(first , second)
        first = second
        second = third
    return third

print(fun(4))