x = list()
y = list()
z = list()
T = int(input())

for i in range(T):
    a = input()
    x.append(a)

for i in range(T-1):
    for j in range(len(x[0])):
        if x[i][j] != x[i+1][j]:
            y.append(j)

for i in range(len(x[0])):
    if i not in y:
        z.append(x[0][i])
    else:
        z.append("?")
ans = "".join(z)
print(ans)