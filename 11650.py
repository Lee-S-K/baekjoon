# 좌표 정렬하기
import sys

put = sys.stdin.readline

T = int(put())
coor = []

for i in range(T):
    x, y = put().split()
    coor.append((int(x), int(y)))

new_coor = sorted(coor, key = lambda x : [x[0], x[1]])

for i in range(T):
    print(new_coor[i][0], new_coor[i][1])