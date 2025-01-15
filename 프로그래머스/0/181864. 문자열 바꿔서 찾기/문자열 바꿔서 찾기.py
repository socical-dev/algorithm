def solution(myString, pat):
    answer = 0
    replace_myString = ""
    
    for v in myString:
        if v in "A":
            replace_myString += "B"
        else:
            replace_myString += "A"
            
    if pat in replace_myString:
        answer = 1
    else:
        answer = 0
    return answer