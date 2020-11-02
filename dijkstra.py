from math import inf

def change_minus_one_to_inf(matr):
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if matr[i][j] == -1:
                matr[i][j] = inf
    return matr


def get_reverse_path(f, s, prev): #  path from finish to start
    path = []
    while f != s:
        path.append(f)
        f = prev[f]

    path.append(s)
    return path


def get_path(f, s, prev):  # path from start to finish
    res = get_reverse_path(f, s, prev)
    res.reverse()
    return res


def dijkstra(graph, n, s, f):
    graph = change_minus_one_to_inf(graph)  # set distances to inf for absent edges

    prev = [s for i in range(n)]  # list of previous points

    dist = [0 for i in range(n)]  # min dist to point i
    for i in range(n):
        dist[i] = graph[s][i]

    dist[s] = 0
    marked = {s}
    vertices = set([v for v in range(n)])

    while marked != vertices:
        min_dist = inf
        for i in vertices-marked:

            if dist[i] <= min_dist:  # == for case when each dist[i]==inf
                min_dist = dist[i]
                w = i
        # w already found   
        marked.add(w)
        for v in vertices - marked:
            if dist[w] + graph[w][v] < dist[v]:
                dist[v] = dist[w] + graph[w][v]
                prev[v] = w

    if dist[f] < inf:
        res_ar = {'length_of_path': dist[f], 'path': get_path(f, s, prev)}
    else:
        res_ar = {'length_of_path': -1, 'path': -1}
    return res_ar


def print_list_as_one_string(my_list):
    res_as_one_str = ""

    for num in my_list:
        res_as_one_str += str(num) + " "

    print(res_as_one_str)


first_input_str_as_list = [int(num) for num in input().split(' ')]
n = first_input_str_as_list[0]
s = first_input_str_as_list[1] - 1
f = first_input_str_as_list[2] - 1
graph = [[] for i in range(n)]
for i in range(n):
    graph[i] = [int(num) for num in input().split(' ')]


res = dijkstra(graph, n, s, f)

print_list_as_one_string([elem + 1 for elem in res['path']])




















