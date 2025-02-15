import sys
from itertools import combinations

input = sys.stdin.readlines()
N, M = map(int, input[0].split())
cards = list(map(int, input[1].split()))

answer = 0

for combo in combinations(cards, 3):    # combinations(cards, 3) => 매개변수 cards 리스트를 3개씩 뭐든 경우의 수 생성 -> combo 변수에 리스트 형식으로 할당
    total = sum(combo)
    if total <= M:
        answer = max(answer, total) # 둘 중에 큰 값을 answer 에 할달

print(answer)