def solution(code):
    # code 의 문자가 "1" 이면 mode 바꿈
    # mode 는 0 또는 1
    # mode 가 0 일 때
    # code[idx] != "1" 일 경우 : idx 가 짝수 일 때만 ret 뒤에 code[ids] 값 추가
    # code[idx] == "1" 일 경우 : mode 를 0에서 1로 바꾼다.
    # 
    # mode 가 1 일 때
    # code[idx] != "1" 일 경우 : idx 가 홀수 일때만 ret 뒤에 code[idx] 값 추가
    # code[idx] == "1" 일 경우 : mode 를 1에서 0으로 바꾼다.
    # 
    # answer 가 빈 문자열일 경우 EMPTY 를 리턴
    answer = ''
    mode = 0    # 시작은 0
    
    for i in range(0, len(code)):
        if mode == 0:
            if code[i] != "1":
                if i % 2 == 0:
                    answer += code[i]
            else:
                mode = 1
        else:
            if code[i] != "1":
                if i % 2 > 0:
                    answer += code[i]
            else:
                mode = 0
        
    if bool(answer) == False:   # bool 함수 안에 문자열을 쓰게 되면 문자열이 비어있는지 아닌지 True, False 로 알려준다.
        answer = 'EMPTY'
    
    return answer


"""
엄청난 분이 푼 코드,,,
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
"""