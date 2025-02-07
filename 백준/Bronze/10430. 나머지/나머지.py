# 첫째 줄 => (A+B) % C
# 둘째 줄 => ((A%C) + (B%C)) % C
# 셋째 줄 => (A*B) % C
# 넷째 줄 => ((A%C) * (B%C)) % C

import sys

A, B, C = map(int, sys.stdin.readline().split())

print(f'{(A+B)%C}\n{((A%C) + (B%C)) % C}\n{(A*B) % C}\n{((A%C) * (B%C)) % C}')