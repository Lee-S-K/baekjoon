# 소트인사이드

import sys

put = sys.stdin.readline

N = list(map(int, put().rstrip()))

N.sort(reverse = True)

for i in range(len(N)):
    print(N[i], end= "")