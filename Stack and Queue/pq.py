import heapq
ram = []

# above is for creating a PQ

heapq.heappush(ram , 55) #TC => O(1)
heapq.heappush(ram , 31)
heapq.heappush(ram , 72)
heapq.heappush(ram , 15)
heapq.heappush(ram , 27)
heapq.heappush(ram , 77)
print(ram)

#dequeue operation
# heapq.heappop(ram)

while len(ram) > 0:
    print(heapq.heappop(ram)) # O(1) deletion


print(ram)