def solution(arr, delete_list):
    """
    arr 리스트 안의 있는 값을 delete_list 리스트 안의 있는 값을 비교하여
    같이 있지 않은 값을 answer 에 추가하여 풀 예정이다.
    """
    answer = []
    for value in arr:
        if value not in delete_list:
            answer.append(value)
    return answer