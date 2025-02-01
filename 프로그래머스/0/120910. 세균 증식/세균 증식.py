def solution(n, t):
    """
    처음 세균 수: n
    경과한 시간: t
    """
    answer = 0
    answer = n
    for _ in range(t):
        answer *= 2
    return answer