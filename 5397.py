T = int(input())

for i in range(0, T):
    Lstack = list()
    Rstack = list()
    x = input()
    for i in x:
        if i == "<":
            if Lstack:
                Rstack.append(Lstack.pop())
        elif i == ">":
            if Rstack:
                Lstack.append(Rstack.pop())
        elif i == "-":
            if Lstack:
                Lstack.pop()
        else: Lstack.append(i)

    Lstack.extend(reversed(Rstack))

    print("".join(Lstack))
    