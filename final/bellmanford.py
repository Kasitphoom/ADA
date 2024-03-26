def bellmanFord():
    
    graph_length = int(input())
    graph = [
        [0 for _ in range(graph_length)]
        for _ in range(graph_length)
    ]
    
    edges = []

    while True:
        edge = list(map(int, input().split()))
        if edge[0] == 0 and edge[1] == 0:
            break
        edges.append([edge[0] - 1, edge[1] - 1, edge[2]])
        
        
    table = [[float("inf") for i in range(graph_length)] for j in range(graph_length)]
    
    table[0][0] = 0
    for n in range(1, graph_length):
        for t in range(graph_length):
            table[n][t] = table[n - 1][t]
        for edge in edges:
            v, t, w = edge
            if table[n - 1][v] + w < table[n][t]:
                table[n][t] = table[n - 1][v] + w
                
        if n == 1:
            table[n][0] = float("inf")
        
        print("======= loop", n, "=======")
        # print tables
        print(*table, sep='\n')
    
    return table[graph_length - 1]

bellmanFord()