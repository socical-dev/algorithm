import sys

sys_input = [n ** 2 for n in map(int, sys.stdin.readline().split())]

print(sum(sys_input) % 10)