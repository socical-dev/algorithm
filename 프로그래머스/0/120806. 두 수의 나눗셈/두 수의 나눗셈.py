def solution(num1, num2):
    """
        # (num1 // num2) * 1000   형변환을 다음과 같이 쓰면 이상한 값이 나오고, 
        (num1 * 1000) // num2 하면 제대로 된 값이 나오네 ㅡㅡ 왜 일까?
        # 방식이 다양할 것 같은데,,
        # int((num1/num2) * 1000) 이렇게 하면 되네,,,
    """
    answer = (num1 * 1000) // num2
    return answer
