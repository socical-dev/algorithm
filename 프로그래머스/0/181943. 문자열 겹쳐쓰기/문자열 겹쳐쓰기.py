def solution(my_string, overwrite_string, s):
    """
    my_string, overwrite_string : 문자열
    s : 정수
    
    my_string[s] ~ len(overwrite_string) 까지는 overwirte_string 으로 해주고, 그 앞은 0 ~ my_string[2] 로 채울 것
    """
    answer = ''
    list_my_string = list(my_string)
    
    del list_my_string[:s+len(overwrite_string)]    # 0 부터 n 개까지 리스트에 요소 삭제
    join_my_string = "".join(list_my_string)    # join 메서드를 통해 , 를 없애고, 문자열 형태로 변환하기 위해 선언
    
    for i in range(0, s):
        answer += my_string[i]
        
    for i in range(0, len(overwrite_string)):
        answer += overwrite_string[i]
    
    answer += join_my_string
        
    return answer