def solution(array, height):
    # 키 리스트 : array
    # 머쓱이의 키 : height
    answer = 0
    for h in array:
        if h > height:
            answer += 1
    return answer