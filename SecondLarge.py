arr = [ -10 , -20, -30, -40, -50] # edge cases
# arr.sort()
# print(arr[-2])  O(nlog(n))

largest = arr[0]
second = arr[1]

for i in range( 0 , len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]
        
print(largest)
print(second)