# Z
import sys
put = sys.stdin.readline

def Z(num, nr, nc):
    global count
    if num == 2:
        if nr == r and nc == c:
            print(count)
            return
        count += 1
        if nr == r and nc + 1 == c:
            print(count)
            return
        count += 1
        if nr + 1 == r and nc == c:
            print(count)
            return
        count += 1
        if nr + 1 == r and nc + 1 == c:
            print(count)
            return
        count += 1
        return
    Z(num/2, nr, nc)
    Z(num/2, nr, nc + num/2)
    Z(num/2, nr + num/2, nc)
    Z(num/2, nr + num/2, nc + num/2)
count = 0
N, r, c = map(int, put().split())
Z(2**N, 0, 0)