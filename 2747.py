# 피보나치 수

import sys

put = sys.stdin.readline

f0, f1 = 0, 1

T = int(put())

for i in range(T-1):

    f = f0 + f1
    f0 = f1
    f1 = f

print(f1)