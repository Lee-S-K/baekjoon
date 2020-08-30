# 0 만들기
import sys
import copy
put = sys.stdin.readline

def operation(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        return

    array.append(" ")
    operation(array, n)
    array.pop()

    array.append("+")
    operation(array, n)
    array.pop()

    array.append("-")
    operation(array, n)
    array.pop()

T = int(put())

for _ in range(T):
    operator_list = []
    n = int(put())
    operation([], n-1)

    num_list = [i for i in range(1, n+1)]

    for operator in operator_list:
        result = ""
        for j in range(n-1):
            result += str(num_list[j]) + operator[j]
        result += str(num_list[-1])
        if eval(result.replace(" ","")) == 0:
            print(result)
    print()
