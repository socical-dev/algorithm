def solution(start_num, end_num):
    answer = []
    # start_num = 10, end_num = 3 일 때 10 부터 1씩 감소하며 3까지 반복문이 돈다.
    # 3까지 나와야 하기에 end_num = end_num-1 이어야 한다.
    for i in range(start_num,end_num-1,-1):
        answer.append(i)
    return answer