arr = [ 6, 0 , 5 , 0 , 3 , 0]
x = 7

left = 0
right = 0
windowSum = 0
minLength = len(arr)

for right in range(0 , len(arr)):
    windowSum = windowSum + arr[right]
    while windowSum >= x:
        minLength = min(minLength , right - left + 1)
        left += 1
        windowSum = windowSum - arr[left - 1]

print(minLength)


