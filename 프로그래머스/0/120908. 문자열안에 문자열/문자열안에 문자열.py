def solution(str1, str2):
    # str2 in str1 이면 1, 없다면 2
    answer = 0
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer