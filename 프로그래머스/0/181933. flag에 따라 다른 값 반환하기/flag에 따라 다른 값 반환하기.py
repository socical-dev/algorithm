def solution(a, b, flag):
    answer = 0
    # flag가 true이면 a + b, false이면 a - b 이기 때문에 flag 를 조건식에 넣어서 사용.
    if flag:
        answer = a + b
    else:
        answer = a - b
    return answer