def solution(a, b):
    """
    - "ab" 와 2*a*b 중 더 큰 값 return
    """
    answer = 0
    str_ab = f'{a}{b}'
    multipl_ab = 2 * a * b
    
    if int(str_ab) >= multipl_ab:
        answer = int(str_ab)
    else:
        answer = multipl_ab
        
    return answer