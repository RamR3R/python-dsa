def fun( n ):
    #base condition
    if n == 1:
        return 1
    
    #recursive call
    return n * fun(n - 1)


number = 5
#sum of the first n numbers
result = fun(number)
print(result)


