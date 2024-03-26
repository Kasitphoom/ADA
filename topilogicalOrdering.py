"""Topological ordering of a directed graph"""
import heapq
from collections import defaultdict
def topological_sort(graph):
    """Perform topological sort on a graph. Return a list of nodes if the graph"""
    in_degree = {u: 0 for u in graph}  # determine in-degree of each node
    for u in graph:                    # for each node
        for v in graph[u]:             # for each neighbor
            in_degree[v] = in_degree.get(v, 0) + 1  # increment in-degree

    Q = []                             # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            heapq.heappush(Q, u)

    L = []                             # list for order of nodes

    while Q:                           # while Q is not empty
        u = heapq.heappop(Q)           # choose node of zero in-degree
        L.append(u)                    # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(Q, v)

    if len(L) == len(graph):
        return L
    else:                               # if there is a cycle,
        return []                       # then return an empty list

def solve():
    """Solve the problem."""
    words = []
    while True:
        word = input().strip()
        if word == '#':
            break
        words.append(word)

    graph = defaultdict(list)
    for i in range(len(words) - 1):
        for a, b in zip(words[i], words[i + 1]):
            if a != b:
                graph[a].append(b)
                break

    order = topological_sort(graph)
    print(''.join(order))

solve()
