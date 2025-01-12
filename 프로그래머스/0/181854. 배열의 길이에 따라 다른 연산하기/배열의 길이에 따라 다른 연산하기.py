def solution(arr, n):
    """
    arr 길이가 짝수 => arr의 모든 홀수 인덱스 위치에 n을 더하고,
    arr 길이가 홀수 => arr의 모든 짝수 인덱스 위치에 n을 더해라 (0도 짝수)
    """
    answer = []
    
    if len(arr) % 2 > 0:    # arr 길이가 홀수 일 때
        for i in range(0,len(arr)):
            if i % 2 == 0 or i == 0:    # 나머지가 없고, 인덱스가 0일 경우
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:   # arr 길이가 짝수 일 때
        for i in range(0,len(arr)):
            if i % 2 > 0:   # 나머지가 있을 경우
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
        
    
    return answer