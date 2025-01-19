def solution(myString):
    """
    - myStrin 을 x 로 split()
    - 각 문자열 길이를 answer 에  append()
    """
    answer = []
    split_myString = myString.split("x")
    
    for str_v in split_myString:
        answer.append(len(str_v))
    
    return answer