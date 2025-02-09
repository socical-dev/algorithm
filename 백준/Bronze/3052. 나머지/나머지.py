# 컴프리헨션 + set 함수(배열 중복 제거)
import sys

code = [int(n.strip())%42 for n in sys.stdin.readlines()]

print(len(set(code)))