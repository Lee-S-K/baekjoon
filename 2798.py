x, y = list(map(int, input().split()))
num = list(map(int, input().split()))
ans = list()

for i in range(0, len(num)-2):
    for j in range(i+1, len(num)-1):
        for k in range(j+1, len(num)):
            result = num[i] + num[j] + num[k]
            if  result <= y:
                ans.append(result)
            
print(max(ans))


