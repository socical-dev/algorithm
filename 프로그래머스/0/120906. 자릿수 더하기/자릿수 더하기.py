def solution(n):
    """
    map(int, str(n)):
    - str(n)의 결과인 '1234'를 한 글자씩 순회하면서 int() 함수를 적용.
    --> 즉, '1', '2', '3', '4' 각각을 int()로 변환하여 [1, 2, 3, 4]라는 리스트가 됨.
    """
    answer = 0
    answer = sum(map(int, str(n)))
    return answer