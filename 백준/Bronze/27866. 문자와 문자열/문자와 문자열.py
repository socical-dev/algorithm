import sys

code = [v.strip() for v in sys.stdin.readlines()]
print(code[0][int(code[1])-1])