def solution(s):
    answer = ''
    s_list = sorted(map(int, s.split()))
    answer = str(s_list[0]) + " " + str(s_list[-1])
    return answer