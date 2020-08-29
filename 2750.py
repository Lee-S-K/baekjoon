# 수 정렬하기

import sys

put = sys.stdin.readline

T = int(put())
n = [int(put()) for _ in range(T)]
n.sort()

for i in range(T):
    print(n[i])