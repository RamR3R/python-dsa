homes = [ 2 , 7 , 9 , 3 , 1]

def fun(n):
    if n < 0:
        return 0
    
    rob = homes[n] + fun(n - 2)
    dontRob = fun(n - 1)

    return max(rob , dontRob)    
print(fun(4))