def solution(arr):
    # answer 리스트에 arr의 요소만큼 반복문을 돌려 해당 요소를 추가하는 문제
    answer = []
    for value in arr:
        for  i in range(0, value):
            answer.append(value)
        # 왜 안된건지 연구 필요,,,
        # str_value = str(value) * int(value)
        # # str_value 문자열은 시퀀스 자료형이기에 리스트이면 리스트 안에 있는 요소를 int 형식으로 변환했다.
        # answer += map(int,str_value)
    return answer