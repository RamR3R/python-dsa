arr = [3 , 4 , 0 , 0 ,8 ]
j = 0
for i in range(0, len(arr)): # O(n) => O(2n) =>O(n)
    if arr[i] == 0:
        j = i
        break

for i in range(j , len(arr)):  # TC => O(n) SC => O(1)
    if arr[i] == 0:
        continue
    else:
        arr[i] , arr[j] = arr[j] , arr[i]
        j += 1
    print(arr) # this line is for debugging
print(arr)