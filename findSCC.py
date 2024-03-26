in1 = input()
graph = { i : [] for i in range(1, int(in1)+1)}
while True:
    in2 = input()
    if in2 == '0 0':
        break
    else:
        node1, node2 = map(int, in2.split())
        if node1 not in graph:
            graph[node1] = []
        graph[node1].append(node2)
        
state = ['UNDISCOVERED' for i in range(1, int(in1)+1)]
low = [0 for i in range(1, int(in1)+1)]
num = [0 for i in range(1, int(in1)+1)]
s = []
onstack = [False for i in range(1, int(in1)+1)]
counter = 0
sccs = []
scc = []


def findscc():
    for i in graph:
        if state[i-1] == 'UNDISCOVERED':
            dfs(i)


def dfs(u):
    global counter
    u -= 1  # subtract 1 to convert to 0-based indexing
    state[u] = 'DISCOVERED'
    counter += 1
    low[u] = num[u] = counter
    s.append(u)
    onstack[u] = True
    for v in graph[u+1]:  # add 1 to convert back to 1-based indexing
        v -= 1  # subtract 1 to convert to 0-based indexing
        if state[v] == 'UNDISCOVERED':
            dfs(v+1)  # add 1 to convert back to 1-based indexing
            low[u] = min(low[u], low[v])
        elif state[v] == 'DISCOVERED': 
            low[u] = min(low[u], num[v])
        elif state[v] == 'EXPLORED':
            if onstack[v]:
                low[u] = min(low[u], num[v])
    
    if low[u] == num[u]:
        scc = []
        while True:
            w = s.pop()
            onstack[w] = False
            
            scc.append(w+1)  # add 1 to convert back to 1-based indexing
            if w == u:
                break
        sccs.append(scc)
    
    state[u] = 'EXPLORED'

findscc()
sccs.sort(key=min)
for i in sccs:
    i.sort()
    print(*i)