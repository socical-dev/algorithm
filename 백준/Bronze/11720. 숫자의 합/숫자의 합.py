# 입력 값을 code에 저장 -> n_list에 code[1]의 여백을 제거해주고, list형식으로 변화 -> 원소 데이터 타입을 int 로 변환 -> sum() 함수로 처리
import sys

code = sys.stdin.readlines()
n_list = map(int, list(code[1].strip()))
print(sum(n_list))