arr = [2, 1, 4 , 3, 5]
result = [1] * len(arr)
#create prefix
prefix = [1] * len(arr)
prefix[0] = 1
for i in range(1 , len(arr)):
    prefix[i] = prefix[i - 1] * arr[i - 1]

#create suffix
suffix = [1] * len(arr)
suffix[len(arr) - 1] = 1
for i in range(len(arr) - 2 , -1 , -1):
    suffix[i] = suffix[i + 1] * arr[i + 1]

for i in range(0 , len(arr)):
    result[i] = suffix[i] * prefix[i]
print(result)