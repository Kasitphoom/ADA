"""Program to find least Articulation points in a graph"""

def art_points(graph, length):
    """Articulation points in a graph."""
    visited = [0 for _ in range(length)]
    parent = [-1 for _ in range(length)]
    low = [0 for _ in range(length)]
    disc = [0 for _ in range(length)]
    articulation_points = [0 for _ in range(length)]
    time = 0

    def dfs(node):
        """Depth First Search."""
        nonlocal time
        children = 0
        visited[node] = 1
        low[node] = disc[node] = time
        time += 1

        for i in range(length):
            if graph[node][i]:
                if not visited[i]:
                    children += 1
                    parent[i] = node
                    dfs(i)
                    low[node] = min(low[node], low[i])
                    if parent[node] == -1 and children > 1:
                        articulation_points[node] = 1
                    if parent[node] != -1 and low[i] >= disc[node]:
                        articulation_points[node] = 1
                elif i != parent[node]:
                    low[node] = min(low[node], disc[i])

    for i in range(length):
        if not visited[i]:
            dfs(i)

    return [i + 1 for i in range(length) if articulation_points[i]]

def main():
    """Main function."""
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
        graph[edge[1] - 1][edge[0] - 1] = 1

    print(*art_points(graph, graph_length))

if __name__ == "__main__":
    main()
