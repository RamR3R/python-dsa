def fun(index , n):

    #bc
    if index == n-1:
        return 1
    if index >= n:
        return 0
    

    return fun(index + 1 , n) + fun(index + 2 , n)


n = 4
print(fun( 0 , n))