def solution(num_str):
    # num_str 안의 있는 요소들을 모두 더한 값을 출력하는 문제
    answer = 0
    for num in num_str:
        answer += int(num)
    return answer