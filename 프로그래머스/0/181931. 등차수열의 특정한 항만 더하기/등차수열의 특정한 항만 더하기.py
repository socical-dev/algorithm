def solution(a, d, included):
    # 첫쨰항: a
    # 공차: d
    # 등차수열: included
    # included 의 요소를 확인하며 공차 d 만큼 증가 한다.
    answer = 0
    v = a
    
    for i in range(0, len(included)):
        if included[i]:
            answer += v
            v += d
        else:
            v += d
            
    return answer