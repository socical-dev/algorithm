def solution(num_list):
    answer = []
    # sorted 함수를 통해 num_list 를 오름차순으로 정렬 후, answer 리스트에 요소 추가
    for i in range(0,5):
        answer.append(sorted(num_list)[i])
    return answer