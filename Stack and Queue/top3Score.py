import heapq
marks = [89 , 90 , 98 , 97 , 45 , 53 , 77 , 84]
# print last n marks of the class from the last
# print top n marks
n = int(input())
pq = []

for i in range(0, len(marks)):
    heapq.heappush(pq, -1 * marks[i])
print(pq)

for i in range(0 , n):
    print(heapq.heappop(pq) * -1)
