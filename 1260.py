# dfs bfs
import sys

V, E, s_node = (map(int, sys.stdin.readline().split()))
graph  = [ [] for _ in range(V+1) ]


for _ in range(E):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, s_node):
    dfs_need_visit, dfs_visited = list(), list()
    dfs_need_visit.append(s_node)

    while dfs_need_visit:
        x = dfs_need_visit.pop()
        if x not in dfs_visited:
            dfs_visited.append(x)
            dfs_need_visit.extend(sorted(graph[x], reverse = True))
        
    return dfs_visited
    

def bfs(graph, s_node):
    bfs_need_visit, bfs_visited = list(), list()
    bfs_need_visit.append(s_node)

    while bfs_need_visit:
        y = bfs_need_visit.pop(0)
        if y not in bfs_visited:
            bfs_visited.append(y)
            bfs_need_visit.extend(sorted(graph[y]))

    return bfs_visited
        

print(" ".join(map(str, dfs(graph, s_node))))
print(" ".join(map(str, bfs(graph, s_node))))