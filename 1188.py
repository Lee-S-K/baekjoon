from math import gcd

x, y = list(map(int, input().split()))

gcdx, gcdy = x/gcd(x,y), y/gcd(x,y)

if gcdx % gcdy == 0:
    print(0)



elif gcdx < gcdy and gcdy % gcdx == 0:
    print(int(gcd(x,y)*(gcdy-gcdx)))
else:
    print(int(gcd(x,y)*(gcdy-1)))
