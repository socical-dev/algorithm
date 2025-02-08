# 컴프리헨션으로 문제 접근!

import sys

sys_content = sys.stdin.readlines()

N = int(sys_content[0].split()[0])
X = int(sys_content[0].split()[1])

answer = [n for n in sys_content[1].split() if X > int(n)]

print(*answer)