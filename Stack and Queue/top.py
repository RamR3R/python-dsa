import heapq
mq = [("Ram" , 0) , ("Virat" , 50) , ("Modi" , 100)]

pq = []

for i in range( 0 ,len(mq)):
    heapq.heappush(pq , ( -1 * mq[i][1] , mq[i][0] ))

print(pq)

while len(pq) > 0:
    print(heapq.heappop(pq)[1])
#op => modi => virat => ram
