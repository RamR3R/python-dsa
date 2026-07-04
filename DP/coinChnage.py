amount = 11
coins = [1 , 2, 5 , 10]
dp = [float("inf")] * (amount + 1)
print(dp)

def fun(amount): # TC => O(n) || Sc => O(n+1)
    # if amount == 0:
    #     return 0
    # if amount < 0:
    #     return float("inf")
    
    # if dp[amount] != -1:
    #     return dp[amount]
    
    # mini = float("inf")
    # for coin in coins:
    #     mini = min(mini , 1 + fun(amount - coin))
    # dp[amount] = mini
    
    dp[0] = 0
    for i in range(1 , amount + 1): # O(n)  || SC => O(n+1)
        for coin in coins: #(k)
            if i - coin >= 0 :
                dp[i] = min(dp[i] ,1 + dp[i - coin])
        


    return dp[amount]

print(fun(amount))