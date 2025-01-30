def solution(slice, n):
    # 피작 조각 수 = slice
    # 피자 먹는 사람 수 = n
    # n 명의 사람이 최소 한 족각 이상 피자를 먹으려면 최소 몇 판?
    # n / slice 의 값 + 1 로 접근
    answer = 0
    answer= n / slice
    
    need_slice = int(n / slice)
    
    if n % slice  > 0:
        answer = need_slice + 1
    else:
        answer = need_slice
    return answer