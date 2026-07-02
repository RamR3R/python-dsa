n = 6 # vertex
edges = [[0 , 1 , 3] , [0 ,2 ,5] , [1,2,-2], [2,3,-4] , [2,5,7] , [ 2,4,-2],[3,5,-2] , [4,5,5]]
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
distance = [float("inf")] * n
distance[src] = 0 # SC => O(V)

for i in range(0 , n - 1): #TC => O(V x E)
    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if distance[u] != float("inf") and distance[v] > distance[u] + w:
            distance[v] = distance[u] + w
    
print(distance)
