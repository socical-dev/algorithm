# 컴프리헨션으로 조건에 맞는 문자열 배열에 저장 -> "3 AAA" 와 같은 문자열이 여러 개 일 수 있기에 반복문 -> "3 AAA" 같은 문자열 split() 으로 자르기 -> 문자 반복 삽입
import sys

code = [n.strip() for n in sys.stdin.readlines() if len(n.split()) == 2]

for c in code:
    s_c = c.split()
    answer = ""
    for s in s_c[1]:
        answer += s*int(s_c[0])
    
    print(answer)