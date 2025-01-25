def solution(n, control):
    answer = 0
    
    n += control.count("w")
    n -= control.count("s")
    n += control.count("d") * 10
    n -= control.count("a") * 10
    
    answer = n
    
    return answer