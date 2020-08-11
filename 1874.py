T = int(input())
stack = list()
result = list()
cnt = 1

for i in range(T):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        result.append("+")
    
    if stack[-1] == data:
        stack.pop()
        result.append("-")
    
    else:
         print("NO")
         exit(0)

print("\n".join(result))