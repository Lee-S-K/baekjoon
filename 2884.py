x, y = input().split()
x = int(x)
y = int(y)
if y<45 and x != 0:
    print("{0} {1}" .format(x-1, y+15))
elif 45<=y<=59:
    print("{0} {1}" .format(x, y-45))
elif y<45 and x == 0:
    print("23 {0}" .format(y+15))
elif y<45 and x != 0:
    print("{0} {1}" .format(x-1, y+15))
else :
    print("23 {0}" .format(y+15))
    