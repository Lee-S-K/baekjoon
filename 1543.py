# 문서 검색
import sys
import copy
put = sys.stdin.readline

text = put().rstrip()
text_find = put().rstrip()
result = []
result.append(text)
count = 0

while 1:
    if result[count].find(text_find) != -1:
        result.append(result[count][result[count].find(text_find)+len(text_find):])
        count +=1
    else :
        break
    
print(count)