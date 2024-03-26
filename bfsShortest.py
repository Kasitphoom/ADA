"""BFS Shortest Path Algorithm non weighted graph"""
def bfs_shortest():
    """Graph Transversal function"""
    graph_length = int(input())
    starting_node, destination_node = map(int, input().split())
    graph = [
        [0 for _ in range(graph_length)]
        for _ in range(graph_length)
    ]

    while True:
        edge = list(map(int, input().split()))
        if edge == [0, 0]:
            break
        graph[edge[0] - 1][edge[1] - 1] = 1

    queue = [starting_node - 1]
    visited = [0 for _ in range(graph_length)]
    back = [None for _ in range(graph_length)]
    found = False

    visited[starting_node - 1] = 1
    while queue and not found:
        node = queue.pop(0)
        for i in range(graph_length):
            if graph[node][i] and i == destination_node - 1:
                back[i] = node
                found = True
                break
            if graph[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                back[i] = node

    if found:
        path = [destination_node]
        while path[-1] != starting_node:
            path.append(back[path[-1] - 1] + 1)

        print(*path[::-1])
    else:
        print("No path")

bfs_shortest()
