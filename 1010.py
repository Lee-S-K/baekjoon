def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)
    
T = int(input())

for i in range(T):
    x,y = map(int, input().split())
    print(int(factorial(y)/(factorial(y-x)*factorial(x))))
