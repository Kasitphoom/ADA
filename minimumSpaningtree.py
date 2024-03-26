"""Minimum Spanning Tree"""
import heapq

in1 = input()
nodes= { i : [] for i in range(1, int(in1)+1)}
graph = { i : [] for i in range(1, int(in1)+1)}

for i in range(1, int(in1)+1):
    in2 = input()
    corx, cory = map(int, in2.split())
    nodes[i].append(corx)
    nodes[i].append(cory)

for i in range(1, int(in1)+1):
    for j in range(1, int(in1)+1):
        if i != j:
            x1, y1 = nodes[i]
            x2, y2 = nodes[j]
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            graph[i].append((j, dist))


def kruskal(graph):
    """Kruskal's algorithm for minimum spanning tree."""
    mst = []
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((w, u, v))
    edges.sort()
    parent = {i: i for i in graph}
    rank = {i: 0 for i in graph}

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        rootu = find(u)
        rootv = find(v)
        if rank[rootu] > rank[rootv]:
            parent[rootv] = rootu
        else:
            parent[rootu] = rootv
            if rank[rootu] == rank[rootv]:
                rank[rootv] += 1

    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    return mst

mst = kruskal(graph)
total = 0
for u, v, w in mst:
    total += w
    
print(round(total, 2))