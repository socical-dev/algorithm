def solution(n):
    # n ** 1 은 n 의 제곱수이기에 0.5 로 n 제곱수의 정수를 찾으려고 접근
    # 제곱수가 아니라면 소숫점이 남아있을 것이기에 나머지가 0 이면 제곱근이고, 아니면 제곱근이 아닌 걸로 접근
    answer = 0
    if n ** 0.5 % int(n ** 0.5) == 0:
        answer = 1
    else:
        answer = 2
    return answer