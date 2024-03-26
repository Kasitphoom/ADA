"""Graph Transversal function"""
UNDISCOVERED = 0
DISCOVERED = 1

graph_length = int(input())
graph = [
    [0 for _ in range(graph_length)]
    for _ in range(graph_length)
]

while True:
    edge = list(map(int, input().split()))
    if edge == [0, 0]:
        break
    graph[edge[0] - 1][edge[1] - 1] = 1

visited = [UNDISCOVERED for _ in range(graph_length)]
queue = []
result = []

queue.append(0)

while queue:
    n = queue.pop(0)
    result.append(n + 1)
    visited[n] = DISCOVERED
    
    for v in range(graph_length):
        if not visited[v] and graph[n][v]:
            queue.append(v)
            visited[v] = DISCOVERED

print(*result)