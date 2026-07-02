arr = [3 , 2 , 7 , 8 , 1 , 0]
n = len(arr)

for i in range(1 , n): #TC => O(n^2)
    pointer = i
    while pointer > 0 and arr[pointer-1] > arr[pointer]:
        arr[pointer] , arr[pointer-1] = arr[pointer-1] , arr[pointer]
        pointer = pointer - 1

print(arr)