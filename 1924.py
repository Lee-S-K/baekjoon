day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
thirtyone = [1, 3, 5, 7 ,8, 10, 12]
thirty = [4, 6, 9, 11]
twentyeight = [2]
m, d = map(int, input().split())
i = 1
n= 0
while i < m:   

    if i in thirtyone:
        n += 31

    elif i in thirty:
        n += 30

    elif i in twentyeight :
        n += 28

    i += 1

x = (n+d)%7

print("{0}".format(day[x-1]))