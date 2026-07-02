import heapq
n = 6 # vertex
edges = [[0 , 1 , 3] , [0 ,2 ,5] , [1,2,3], [2,3,4] , [2,5,7] , [2,4,2],[3,5,2] , [4,5,5]]
graph = {}
for i in range(0, n):
    graph[i] = []
print(graph)
#construct our graph
for edge in edges:
    u = edge[0]
    v = edge[1]
    w = edge[2]
    graph[u].append([v , w])
    #undirected graph
    graph[v].append([u , w])
print(graph)
src = 0
pq = []

heapq.heappush(pq , (0 , src))

distance = [float("inf")] * n #SC => O(V + E)

while len(pq) > 0: #TC => O((V + E)(log V))
    x = heapq.heappop(pq)
    currDistance = x[0]
    node = x[1]
    if distance[node] < currDistance:
        continue
    distance[node] = currDistance
    for neighbour in graph[node]:
        nextDistance = currDistance + neighbour[1]
        print(node , nextDistance , neighbour[0])
        v = neighbour[0]
        if distance[v] > nextDistance:
            heapq.heappush(pq , (nextDistance , v))

print(distance)

