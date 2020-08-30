# 수 정렬하기 2
import sys
put = sys.stdin.readline

T = int(put())
n = [int(put()) for i in range(T)]
n.sort()

for i in n:
    print(i)