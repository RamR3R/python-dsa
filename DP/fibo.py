count = 0
dp = [-1] * 7
def fibo(n): #bottom => top TC => O(n) || SC => O(n)
    # if n <= 1:
    #     return n
    # if dp[n] != -1:
    #     return dp[n]

    # dp[n] = fibo(n - 1) + fibo(n - 2)
    # dp[0] = 0
    # dp[1] = 1

    # for i in range(2, n + 1):  #TC => O(n) || SC => O(n)
    #     dp[i] = dp[i - 1] + dp[i - 2]

    # return dp[n]

    first = 0
    second = 1
    for i in range(2,n+1): # Tc => O(n) || SC => O(1)
        third = first + second
        first = second
        second = third
    return third

    


print(fibo(6))
    
