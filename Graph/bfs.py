from collections import deque
n = 5 # vertex
edges = [[1,2] , [2,4] , [3,4] , [4,5] , [1,4]]
graph = {}
for i in range(1, n + 1):
    graph[i] = []
print(graph)
#construct our graph
for edge in edges:
    u = edge[0]
    v = edge[1]
    graph[u].append(v)
    #undirected graph
    graph[v].append(u)
print(graph)

q = deque()
q.append(1)
visited = set()
while len(q) != 0:
    node = q.popleft()
    visited.add(node)
    print(node , end = " => ")
    for v in graph[node]:
        if v not in visited:
            q.append(v)