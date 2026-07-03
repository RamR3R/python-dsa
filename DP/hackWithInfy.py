import heapq
n = 3
m = 5

food = [5,7,9]
decay = [2,4,6]
count = [0] * len(food)
pq = []
total = 0
for i in range( 0, len(food)):
    heapq.heappush(pq, (-1 * food[i] , i))


while len(pq) != 0 and m > 0:

    x = heapq.heappop(pq)
    index = x[1]
    value = -1 * x[0]
    total += value
    
    decayedFood = food[index] - (decay[index] * (count[index] + 1))
    count[index] += 1 
    if decayedFood >0:
        heapq.heappush(pq , (-1 * decayedFood , index))

    m -= 1

    print(pq, total)
