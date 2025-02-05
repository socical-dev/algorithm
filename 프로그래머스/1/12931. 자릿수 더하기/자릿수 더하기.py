def solution(n):
    answer = 0
    # map 함수를 통해 "123" 같이 정수를 문자열로 변환한 후 문자 단위로 잘라 int 로 변환하는 방식으로 접근
    answer = sum(map(int, str(n)))

    return answer