n = int(input())
m = int(input())
p = int(input())
# for i in range( 0 , n):   # => O(n x n x n) 
#     for j in range(0 , n):
#         print(i + j)

# for i in range(0, n):
#     print(i)




#sum of the digits
l = [143, 345 ,679]
for i in range(0 , 3):
    sum = 0
    n = l[i]
    
    while n > 0:
        sum = n%10
        n = n // 10
    print(sum)

