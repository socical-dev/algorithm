import sys

input = sys.stdin.readline

# 입력 받은 값에서 '/' 기준으로 나눈 값들을 나눈 다음에 int 형으로 변환 후 k, d, a 에 하나씩 넣어줘.
k, d, a = map(int, input().split('/'))
answer = ""
if d == 0 or k + a < d:
    print("hasu")
else:
    print("gosu")