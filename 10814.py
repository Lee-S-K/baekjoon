# 나이순 정렬

import sys

put = sys.stdin.readline

T = int(put())
person = []

for i in range(T):
    age, name = put().split()
    person.append([int(age), name])

person_array = sorted(person, key = lambda x: x[0])
    
for i in range(T):
    print(person_array[i][0], person_array[i][1])