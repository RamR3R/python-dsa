arr = []

for i in range( 0 , 3):
    temp = []
    for j in range(0 , 3):
        temp.append(0)
    
    arr.append(temp)
arr[0][0] = 5
print(arr)