def floyd_warshall():
    graph_length = int(input())
    graph = [[float('inf') for i in range(graph_length)] for j in range(graph_length)]
    
    for i in range(graph_length):
        graph[i][i] = 0
    
    
    while True:
        edge = input()
        if edge == '0 0 0':
            break
        else:
            node1, node2, weight = map(int, edge.split())
            graph[node1][node2] = weight
    
    print(*graph, sep='\n')
    
    for k in range(graph_length):
        print("===============", k, "=================")
        for i in range(graph_length):
            for j in range(graph_length):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print(*graph, sep='\n')
    
floyd_warshall()