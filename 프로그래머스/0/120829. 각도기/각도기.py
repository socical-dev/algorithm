def solution(angle):
    # 예각 (0~90도 미만) = 1
    # 직각 (90도) = 2
    # 둔각 (90~180도 미만) = 3
    # 평각 = 4 (180도)
    answer = 0
    
    if angle == 180:
        answer = 4
    elif 90 < angle < 180:
        answer = 3
    elif angle == 90:
        answer = 2
    else:
        answer = 1
    return answer