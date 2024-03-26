"""Bipartite graph algorithms."""
def bipartite():
    """Bipartite graph algorithm."""
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

    queue = [0]
    visited = [0 for _ in range(graph_length)]
    color = [0 for _ in range(graph_length)]
    is_bipartite = True

    while queue and is_bipartite:
        node = queue.pop(0)
        for i in range(graph_length):
            if graph[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                color[i] = not color[node]
            elif graph[node][i] and color[i] == color[node]:
                is_bipartite = False
                break

    if is_bipartite:
        # list every 0 in the color list
        print(*[i + 1 for i in range(graph_length) if not color[i]])
        # list every 1 in the color list
        print(*[i + 1 for i in range(graph_length) if color[i]])
    else:
        print("Not possible")

bipartite()
