arr = [ 1, 2, 3 , 4 , 5]
k = 3
n = len(arr)
res = [0 , 0, 0, 0, 0]

for i in range(0 , n):
    res[(i + k) % n] = arr[i]

print(res)