def merge(arr1 , arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def msort(arr):
    #base condition
    if len(arr) <=1:
        return arr # as the length is 1 its already sorted
    
    mid =  len(arr) // 2
    left = msort(arr[:mid])
    right = msort(arr[mid :])
    return merge(left , right)

arr = [3 , 0 , 2, 1 , 5 , 7]
print(msort(arr))
