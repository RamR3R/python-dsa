arr = [4 , 12, 5 , 3, 1, 2, 5, 3, 1, 2, 4]
n = len(arr)
stack = []
res = [-1] * n

for i in range(n-1 , -1 , -1):
    while len(stack) > 0 and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if len(stack) > 0:
        res[i] = stack[-1] - i
    stack.append(i)

print(res)
    
    

    


