arr = [3 , 2, 1 , 4, 5 ,9]
k = 3
windowSum = 0
for i in range(k):
    windowSum += arr[i]

left = 0
right = k - 1
maxii = 0
while right < len(arr):
    left += 1
    right += 1
    
    windowSum = windowSum + arr[right] - arr[left - 1]
    if maxii > windowSum:
        maxii = windowSum
    
print(maxii)

















# windowSum = 0
# left = 0
# right = k - 1
# for i in range( 0 , k):
#     windowSum = windowSum + arr[i]
# maxSum = windowSum

# while right < len(arr) - 1:
#     left += 1
#     right += 1
#     windowSum = windowSum + arr[right] - arr[left - 1]
#     if maxSum < windowSum:
#         maxSum = windowSum
# print(maxSum)
