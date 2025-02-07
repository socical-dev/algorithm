import sys

A, B, C = map(int, sys.stdin.readlines())

print(f"{A+B-C}\n{int(str(A)+str(B))-C}")