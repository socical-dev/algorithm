def solution(my_string):
    answer = ''
    answer = "".join([i for i in my_string if not i in "aeiou"])
    return answer