def solution(num_list):
    """
    num_list 리스트에서 홀수는 서로 이어 붙여 하나의 숫자로 만들고,
    짝수는 서로 이어 붙여 하나의 숫자로 만들어
    홀수 + 짝수를 더한 값
    """
    answer = 0
    even_num = ""   # 짝수
    odd_num = ""    # 홀수
    
    for num in num_list:
        if num % 2 > 0:
            odd_num += str(num)
        else:
            even_num += str(num)
    
    answer = int(even_num) + int(odd_num)
    
    return answer