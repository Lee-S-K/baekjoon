# 수 찾기
import sys

N = int(sys.stdin.readline())
val = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
isval = list(map(int, sys.stdin.readline().split()))

for i in isval:
    if i not in val:
        print('0')
    else:
        print('1') 
