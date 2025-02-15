import sys

N = int(sys.stdin.readline())  # 빠른 입력

count = [0] * 10001  # 숫자의 등장 횟수를 저장할 리스트 (0~10000)

# 입력값을 카운팅
for _ in range(N):
    num = int(sys.stdin.readline())  # 빠른 입력
    count[num] += 1  # 해당 숫자 카운트 증가

# 결과 출력
for num in range(10001):  # 0부터 10000까지
    if count[num] > 0:  # 해당 숫자가 나왔다면
        for _ in range(count[num]):  # 등장한 횟수만큼 출력
            print(num)
