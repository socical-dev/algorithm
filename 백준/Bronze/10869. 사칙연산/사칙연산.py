import sys

A, B= map(int, sys.stdin.readline().split())
        
print(f"{A+B}\n{A-B}\n{A*B}\n{A//B}\n{A%B}")