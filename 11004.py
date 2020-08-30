# K번째 수
import sys
put = sys.stdin.readline

T, n = map(int, put().split())
num_list = list(map(int, put().split()))
num_list.sort()

print(num_list[n-1])