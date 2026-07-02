#stack implementation using list
stack  = []

# 10 20 30 40 50

#push() 
stack.append(10) # TC => O(1)
stack.append(20)
stack.append(30)
print(stack)

#pop()
stack.pop()  # TC => O(1)
print(stack)
stack.pop()
print(stack[-1])
stack.pop()
print(stack[-1])
stack.pop()
print(stack[-1])

#peek()
print(stack[len(stack) - 1])  # TC => O()
print(stack[-1])


#check if stack is empty or not

# isEmpty() =>
if len(stack) == 0: # is equal to insEmpty()
    pass