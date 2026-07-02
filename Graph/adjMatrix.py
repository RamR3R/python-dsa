n = 5 # vertex
edges = [[0,1] , [1,3] , [2,3] , [3,4] , [0,3]]
adjMatrix = [[0] * n for _ in range(0 , n) ] # SC => O(v^2)
for edge in edges:
    u = edge[0]
    v = edge[1]
    #directed
    adjMatrix[u][v] = 1
    #un directed graph
    adjMatrix[v][u] = 1

print(adjMatrix)
