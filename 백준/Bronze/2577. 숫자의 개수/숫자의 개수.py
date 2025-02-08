# A * B * C 의 결과에 0 ~ 9 숫자가 각각 몇 번 쓰였는지 출력
# 문자열의 특정 문자의 갯수를 확인하는 count() 메서드 사용
import sys

sys_input = sys.stdin.readlines()

A = int(sys_input[0].strip())
B = int(sys_input[1].strip())
C = int(sys_input[2].strip())

str_multiple = str(A * B * C)

for n in range(10):
    print(str_multiple.count(f"{n}"))
