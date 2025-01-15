def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2 == 0:  # 짝수 인덱스인 경우
            arr = arr[:q + 1]  # q번 인덱스 포함, 뒷부분 자르기
        else:  # 홀수 인덱스인 경우
            arr = arr[q:]  # q번 인덱스 포함, 앞부분 자르기
    return arr