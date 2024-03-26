"""Graph Transversal"""
def graph_transversal():
    """Graph Transversal function"""
    graph_length = int(input())
    starting_node = int(input())
    graph = [
        [0 for _ in range(graph_length)]
        for _ in range(graph_length)
    ]

    while True:
        edge = list(map(int, input().split()))
        if edge == [0, 0]:
            break
        graph[edge[0] - 1][edge[1] - 1] = 1

    stack = [starting_node - 1]
    visited = []

    while stack:
        node = stack.pop()
        for i in range(graph_length):
            if graph[node][i] and i not in visited:
                stack.append(i)
                visited.append(i)

    print(*[i + 1 for i in sorted(visited)])

graph_transversal()
