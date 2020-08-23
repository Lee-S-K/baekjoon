import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = list()
x, y = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(x)]

def bfs(matrix):
    queue.append([0,0])
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < x and 0 <= nb < y and matrix[na][nb] == 1:
               queue.append([na,nb])
               matrix[na][nb] = matrix[a][b] + 1
            
            

bfs(matrix)

print(matrix[x-1][y-1])
