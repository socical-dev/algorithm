import sys
import math
A, B, V = map(int, sys.stdin.readline().split())

# 정상에 도달하기 전까지 걸리는 날 수 + 마지막 날 + 1
day = math.ceil((V - A) / (A - B)) + 1

print(day)