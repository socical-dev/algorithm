def solution(ineq, eq, n, m):
    """
    두 문자열 : ineq, eq
    ineq = "<" 또는 ">" 중 하나
    eq = "=" 또는 "!" 중 하나
    
    두 정소 : n, m
    
    'n' imeq eq 'm' 의 조건이 맞으면 1 틀리면 0
    """
    answer = 0
    
    if ineq == "<":
        if eq == "=":
            if n <= m:
                answer = 1
            else:
                answer = 0
        else:
            if n < m:
                answer = 1
            else:
                answer = 0
    else:
        if eq == "=":
            if n >= m:
                answer = 1
            else:
                answer = 0
        else:
            if n > m:
                answer = 1
            else:
                answer = 0
                
    return answer