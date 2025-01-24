def solution(myString):
    answer = ''
    answer = myString.replace(myString, myString.lower())
    answer = answer.replace("a", "a".upper())
    return answer