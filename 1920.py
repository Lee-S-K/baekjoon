import sys

N = int(sys.stdin.readline())
val = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
isval = list(map(int, sys.stdin.readline().split()))

for i in isval:
    if i not in val:
        print('0')
    else: print('1') 

# n = int(input())
# array = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i not in array:
#         print('0')
#     else:
#         print('1')