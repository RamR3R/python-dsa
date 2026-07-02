v = 5
edges = [[1,2] , [2,3] , [3,4] , [4,5] , [3,5]]


graph = {}

for i in range(1,  v + 1):
    graph[i] = []

for edge in edges:
    u = edge[0]
    v = edge[1]

    graph[u].append(v)
    graph[v].append(u)

print(graph)
def dfs(node , parent , visited):
    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            if dfs(v , node  , visited) == True:
                return True
        else:
            if v != parent:
                return True
    return False
    


    
print(dfs(1 , -1 , set()))
