cnt = 5
y= 0
while cnt:
    x=int(input())
    if x < 40:
        x = 40
    else:
        pass
    y += x
    cnt -= 1

print(int(y/5))