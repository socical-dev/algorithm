def solution(strArr):
    # strArr 안에 있는 요소를 가지고 조건문을 통해 해당 값에 ad 가 들어있는지 확인 후 없으면 answer에 append()
    answer = []
    
    for v in strArr:
        if "ad" not in v:
            answer.append(v)
        
    return answer