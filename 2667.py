# 단지번호붙이기

import sys

width = int(sys.stdin.readline())
matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(width)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

areacount = []
visit = []

def bfs(x, y):
    matrix[x][y] = 0
    count = 1
    visit.append([x,y])
    
    while visit:
        a = visit[0][0] 
        b = visit[0][1] 
        visit.pop(0)
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < width and 0<= ny < width and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                visit.append([nx, ny])
                count += 1
        
    areacount.append(count)
                    

for x in range(width):
    for y in range(width):
        if matrix[x][y] == 1:
            bfs(x, y)

print(len(areacount))
print("\n".join(map(str, sorted(areacount))))
   
