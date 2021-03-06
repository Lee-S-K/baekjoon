# baekjoon
## Algorithm

## python 유용한 코드
- 내장 함수
```Python code
max(), min(): 시퀀스 자료형에 포함되어 있는 원소 중 최대값 ,최소값 출력
bin(), hex(): 10진수 -> 2진수 변환, 10진수 -> 16진수 변환
print(int('0xe6',16)) # 10진수로 재변환 (값, 진수)
round(): 반올림을 수행 # round(반올림할 값, 반올림할 자릿수) -1은 소숫점 이상에서 반올림
type(): 자료형의 종류 출력
```
***
- 문자열 함수
```python code
print(str[::-1]): 문자열 뒤집기
len(): 문자열 길이 출력
isalpha(): 특정 문자열이 문자로만 이루어져 있는지 확인
isdigit(): 특정 문자열이 숫자로만 이루어져 있는지 확인
isalnum(): 특정 문자열이 문자와 숫자로만 이루어져 있는지 확인
join(): 여러 문자열을 구분문자와 함께 합치는 함수
ex) list = ["x", "y", "z"]
    print(".",join(list))

    int로 된 리스트 출력하기 !!!!!!!
    print(" ".join(map(str, dfs(graph, s_node))))
    print(" ".join(map(str, bfs(graph, s_node))))

sorted(문자열 자료형): 각 문자를 정렬하는 함수
문자열.split(토큰): 문자열을 토큰에 따라서 분리하는 함수
문자열.find("찾을 문자" , 인덱스 번호) 
# 해당 문자가 있다면 가장 앞에 글자의 인덱스 반환 아니면 -1
# 두번쨰 매개변수는 해당 인덱스 다음에서 찾는다는 의미
문자열.upper(): 대문자로 변환
문자열.lower(): 소문자로 변환
문자열.strip(토큰): 문자열에서 양끝에 있는 토큰을 제거해준다 
# lstrip(), rstrip() 매개변수 없을시 공백만 지운다
eval(): 문자열 수식 계산 해준다.
    ex) exp = "36346345+1212*3535"
        print(eval(exp))
```
***
- 리스트 함수
```Python code
list.index("찾을 문자"): 해당 값의 인덱스를 반환
list.reverse(): 해당 문자열 뒤집기
sum(list): 리스트의 모든 원소의 합 반환
range(시작,끝) : 시작부터 끝-1까지
# list = range(5,10) 일때 [5, 6, 7, 8, 9]로 저장됨
list = [True, False, True] 일때
all(list): 모두 참인지 판별, any(list): 하나라도 참이 있는지 판별 
enumerate(list): 리스트에서 인덱스와 원소를 함께 추출
list.sort() # 오름차순으로 정렬
list.count("찾고싶은 문자"): 원소 개수를 추출
del list[인덱스] # 슬라이싱도 가능
list.insert(인덱스 위치, "삽입할 문자")
list.append("넣을 값"): 가장 마지막에 삽입
list.pop(): 가장 마지막 원소 삭제후 반환

```
***
- 유용한 코드
```Python code
new = [(idx, i) for idx, i in enumerate arr]
# idx = 인덱스 i 는 value arr = [5, 6, 7, 8] 일때
# [(0, 5), (1, 6), (2, 7), (3, 8)] 형태의 배열 생성

new = max(arr, key=lambda x: x[0])[0]
# 2차원 리스트에서 열의 첫번째 값이 가장 큰 원소를 리턴
```
***
# 입출력
- input() x sys.stdin.readline()을 사용 : 입출력 속도가 젤 빠름
<br>

- 여러라인 입력 받을 시:
```python code
import sys 
n = input()
a = [sys.stdin.readline() for i in range(n)]
 # a = ["1 2 3", "4 5 6"]
 "Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다."
 ex) matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(x)]
```

- 재귀함수가 있는 경우, 최대 재귀 깊이를 설정
```python code
import sys sys.setrecursionlimit(10**8) 
# 10^8 까지 늘림.
```

- 인접 행렬 체크
```python code
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(matrix):
    queue.append([0,0])
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < x and 0 <= nb < y and matrix[na][nb] == 1:
               queue.append([na,nb])
               matrix[na][nb] = matrix[a][b] + 1
```

# lambda
- lambda 인자: 표현식
- 사용예시: 
    - 백준 10814: 나이순으로 정렬 후 나이가 같을시 들어온 순서대로 정렬:
    ```
    person_array = sorted(person, key = lambda x: x[0])
    ```
    - 백준 1966: z에 인덱스를 저장해서 튜플로 만든 후, 원소들의 첫번째 인덱스끼리 비교하여 max값을 찾은 후 그 max값이 현재 첫번째 원소와 같다면 break
    ```
    max(z, key=lambda x: x[0])[0]:
    ```

    - 백준 11650: x좌표를 기준으로 정렬하고 만약 x좌표가 동일할 시 y좌표를 기준으로 비교한다.
    ```
    new_coor = sorted(coor, key = lambda x : [x[0], x[1]]) 
    // x[0] x좌표,  x[1] y좌표
    ```

# deepcopy
- 리스트를 다른 리스트에 append할때 내장함수 copy를 불러와서 deepcopy 사용
```
import copy
operator_list = []
array = [1, 2, 3]
operator_list.append(copy.deepcopy(array))
```