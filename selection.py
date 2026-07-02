arr = [4 , 5 , 0 , 1 , 3]
n = len(arr)

for i in range(0 , n):
    minIndex = i
    for j in range(i + 1 , n):
        if arr[minIndex] > arr[j]:
            minIndex = j
    arr[i] , arr[minIndex] = arr[minIndex] , arr[i]

print(arr)
