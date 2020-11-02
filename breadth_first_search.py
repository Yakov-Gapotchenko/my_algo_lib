from math import inf
from collections import deque



def bfs(graph, a, n):
    Q = [a]
    dist = [inf for i in range(n)]
    dist[a] = 0
    while len(Q) != 0:

        u = Q.pop(0)
        # for each (u, v) from G
        for v in range(n):
            if graph[u][v] == 1:  # edge (u, v)
                if dist[v] == inf:
                    dist[v] = dist[u] + 1
                    Q.append(v)

    return dist


n = 3
print(bfs([[0, 1, 1], [1, 0, 0], [1, 0, 0]], 1, n))



