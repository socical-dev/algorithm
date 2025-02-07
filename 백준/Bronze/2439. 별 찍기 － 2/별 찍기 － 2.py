# N 줄에 별 N 만큼 별 찍기
import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    print(f'{" "*(N-i)}{"*"*i}')