def solution(n):
    # n은 홀수, n >= 홀수인 모든 양의 정수의 합
    # n은 짝수: n >= 짝수인 모든 양의 정수의 제곱의 합
    # n = 7, 7+5+3+1
    # n = 10
    answer = 0
    for i in range(1, n+1):
        if n != 1 and n%2 == 0: # 짝수 조건문으로 n%2로 나머지가 0이면서 1이 아닌 경우(n=1일 경우에도 0 이기며, 홀수이기에 조건식에 추가)
            if i%2 == 0:    #i가 짝수인지 판별
                answer += i*i
        else:
            if i%2 == 1:    #i가 홀수인지 판별
                answer += i
    return answer