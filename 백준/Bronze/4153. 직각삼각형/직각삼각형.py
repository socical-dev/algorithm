# 직각삼각형 조건: A**2 + B**2  = C**2(빗변)

import sys

input = [v.strip() for v in sys.stdin.readlines() if v.strip() != "0 0 0"]

for v in input:
    A, B, C = sorted(map(int, v.split()))
    if A**2 + B**2 == C**2:
        print("right")
    else:
        print("wrong")
