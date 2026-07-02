arr = [1 , 2, 5 , 7 , 8 , 10]
target = 12
n = len(arr)

# for i in range(0 , n): # O(n x n) => TC => O(n^2)
#     for j in range(i + 1 , n): 
#         if arr[i] + arr[j] == target:
#             print(arr[i] , arr[j])

left = 0
right = n - 1

while left < right:
    sum = arr[left] + arr[right]
    if sum == target:
        print(arr[left] , arr[right])
        left += 1
    elif sum < target:
        left += 1
    elif sum > target:
        right -= 1


