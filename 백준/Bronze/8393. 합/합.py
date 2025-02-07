# 1 ~ n 까지의 합
# 컴프리핸션으로 접근
import sys

n = int(sys.stdin.readline())
print(sum([i for i in range(n+1)]))