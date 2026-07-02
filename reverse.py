arr = [ 1, 2, 3 , 4 , 5]
n = len(arr) 
left = 0
right = n - 1

while left < right: # TC => O(n) SC => O(1)
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    left = left + 1
    right = right - 1

print(arr)



# rev = []
# for i in range(len(arr) - 1 , -1 , -1):
#     rev.append(arr[i]) # tc => O(n) and sc => O(n)
# print(rev)