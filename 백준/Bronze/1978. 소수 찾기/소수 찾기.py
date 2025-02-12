# 주어진 n개 중에 소수가 몇 개 인지 찾아 출력
import sys

answer = 0  # 출력값
input = [n.strip() for n in sys.stdin.readlines()]  # readlines 로 여러 줄을 받고 컴프리헨션을 이용해 공백을 제거하여 input 에 리스트에 저장
num = input[0]
prime_nums = list(map(int, input[1].split()))   # 1 2 3 4 식으로 받은 값을 공백 기준으로 쪼개고, 각 원소(요소)들을 str -> int 형식으로 변환 후 리스트에 저장

for p_n in prime_nums:
    count = 0
    for n in range(1, p_n+1):
        if p_n % n == 0:
            count += 1
        else:
            pass
    if count == 2:  # 소수는 1 또는 자기 자신으로만 나누어 지는 값이기에 2일 경우에 answer +1 증가
        answer += 1
        
print(answer)