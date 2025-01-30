def solution(n):
    # n_list 에 컴프리헨션으로 0 ~ n 까지 2의 배수로 넣어 sum 메서드로 호출하는 방식으로 접근
    answer = 0
    n_list = [num for num in range(n+1) if num % 2 == 0]
    answer = sum(n_list)
    return answer