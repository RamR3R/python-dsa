# 0 1 1 2 3 5 8 13 21 34 - 0based index

def fibo(n):
    #base condition
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


number = 8
print(fibo(number))