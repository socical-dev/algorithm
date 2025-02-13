import sys

answer = 0  # 출력값
input = int(sys.stdin.readline())

for n in range(1, input):
    n_sum = sum(int(split_num) for split_num in str(n))
    if  n + n_sum == input:
        answer = n
        break
        
print(answer)