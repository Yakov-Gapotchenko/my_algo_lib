from enum import Enum


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2



def dfs(graph, color, u, n):
    color[u] = Color.GREY
    for v in range(n):
        if graph[u][v] == 1:  # for all (u, v): (u, v) is in G
            if color[v] == Color.WHITE:
                dfs(graph, color, v, n)
    color[u] = Color.BLACK



def DoDFS(graph, n):
    n = 3
    graph = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    color = [Color.WHITE for i in range(n)]
    for u in range(n):
        if color[u] == Color.WHITE:
            dfs(u)












