def solution(arr):
    answer = []
    # 0 ~ arr 크기만큼 반복문을 돌리며, 0번째 또는 이전 숫자와 동일하지 않을 경우에만 위치 반환
    answer = [arr[n] for n in range(0, len(arr)) if n == 0 or arr[n-1] != arr[n]]
    return answer