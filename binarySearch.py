arr = [1, 2, 3, 4 , 5 ,6 ,7 ,8 , 9, 10 , 11]
x = 12
n = len(arr)  #SC => O(1) constant space
left = 0
right = n - 1
found = False
while left <= right : #TC => O(log(n))
    mid = (left + right) // 2
    print( left , right , arr[mid])
    if arr[mid] == x:
        found = True
        break
    elif arr[mid] > x:
        right = mid - 1
    elif arr[mid] < x:
        left = mid + 1

if found:
    print("ya found!!!!! :)")
else:
    print("Not Found :(")


    
