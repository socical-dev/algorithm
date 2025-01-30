def solution(n, k):
    # 인분: n (n*12,000)
    # 음료수: k (k*2,000)
    # 10인분당 음료수 하나 서비스
    answer = 0
    answer = n * 12000
    """
    n = 64인분
    k = 음료수 6캔
    
    64 * 12000
    """
    drink = k
    drink -= int(n / 10)
    
    answer += drink * 2000
        
    return answer