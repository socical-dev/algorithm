import sys
from itertools import combinations

input_list = [int(input().strip()) for _ in range(9)]

# itertiools 라이브러리를 이용하여 combination 사용 (조합)
for i in combinations(input_list, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        exit()