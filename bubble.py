arr = [1 , 2 , 3, 4 , 5]
n = len(arr)
for iteration in range(0 , n):
    swap = False
    for i in range(0 , n-1-iteration ):
        if arr[i] > arr[i + 1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
            swap = True
    if swap:
        continue
    else : 
        break
print(arr)

