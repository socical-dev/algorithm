def solution(num_list):
    # num_list를 오름차순으로 정렬시키고, 제일 작은 숫자 5개를 제외하고, answer 리스트 안에 추가하면 되는 문제.
    answer = []
    
    for i in range(5,len(num_list)):
        answer.append(sorted(num_list)[i])
    return answer