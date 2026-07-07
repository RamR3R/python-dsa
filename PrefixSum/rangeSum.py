arr = [-1 , 2 , 4 ,1 , -3 , -6]
n = 6
query = [(0,3) , (0,5) , (4,5) , (1,3) , (1,4)]
# [6, -3, -9, 7, 4]
prefix = [0] * n
prefix[0] = 0
ans = [0] * len(query)
for i in range( 1 , len(arr)): # O(n)
    prefix[i] = prefix[i - 1] + arr[i - 1]
print(prefix)
for i in range(0 , len(query)): # O (q)  
    left = query[i][0]
    right = query[i][1]
    ans[i] = prefix[right] - prefix[left] + arr[right]

print(ans) #O(n) || SC => O(n)
# [4, 5, 1, 7, 4]