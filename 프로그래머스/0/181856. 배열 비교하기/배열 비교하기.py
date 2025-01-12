def solution(arr1, arr2):
    """
    - arr2 가 arr1 보다 크면 -1이고, 반대로 arr1이 크면 1, 같다면 원소의 합을 합산해 제일 큰 리스트가 1, 같다면 0 호출
    """
    answer = 0
    
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        if sum(arr1) < sum(arr2):
            answer = -1
        elif sum(arr1) > sum(arr2):
            answer = 1
        else:
            answer = 0
            
    return answer