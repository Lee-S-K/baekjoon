T = int(input())



for i in range(T):
    x, y = list(map(int, input().split()))
    z = list(map(int, input().split()))
    z = [(i, idx) for idx, i in enumerate(z)]
    count = 0
    while True:

        if z[0][0] == max(z, key=lambda x: x[0])[0]:
            count += 1
            if z[0][1] == y:
                print(count)
                break
            else:
                z.pop(0)
        else:
            z.append(z.pop(0))