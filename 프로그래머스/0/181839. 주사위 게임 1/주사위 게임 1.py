def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:   # a와 b 모두 홀수 일 경우
        answer = a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0:  # a 또는 b 중에 하나라도 홀수 일 경우
        answer = 2*(a + b)
    else:   # a와 b 모두 홀수가 아닐 경우(짝수)
        if a > b:
            answer = a - b
        else:
            answer = b - a
        
        
    return answer