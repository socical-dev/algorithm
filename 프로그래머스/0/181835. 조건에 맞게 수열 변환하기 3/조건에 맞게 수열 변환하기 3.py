def solution(arr, k):
    answer = []
    
    # k가 홀수이면 각 원소 * k / 짝수이면 각 원소 + 1
    # 매개변수 arr의 길이 범위 만큼 0부터 반복문을 돈다. 
    for i in range(len(arr)):
        if k == 1 or k%2 == 1:  # 홀수일 경우 (k가 1이거나 k를 2로 나누었을 때 나머지가 1일 경우)
            answer.append(arr[i] * k)
        else:
            answer.append(arr[i] + k)
    return answer