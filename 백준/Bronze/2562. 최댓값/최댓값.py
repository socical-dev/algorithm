import sys

num = list(map(int, sys.stdin.read().split()))
print(f'{max(num)}\n{num.index(max(num))+1}')