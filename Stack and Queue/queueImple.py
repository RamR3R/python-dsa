# queue = []

# # Enqueue => O(1)
# queue.append(10)
# queue.append(15)
# queue.append(17)

# print(queue)

# # Dequeue => O(n)
# queue.pop(0)
# print(queue)

# # Peek => O(1)
# print(queue[0])

# #isEmpty => O(1)
# # len(queue) == 0 => True || False



from collections import deque
q = deque() # creating my queue
#Enqueue
q.append(10) # => [10] => O(1)
q.append(15)
q.append(18)
print(q)
#Dequeue TC => O(1)
q.popleft() # => remove the element from the front of the queue 
print(q)
#peak => front  TC => O(1)
print(q[0])



#isEmpty
