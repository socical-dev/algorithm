number = int(input())

answer = 0

for i in range((len(str(number))//2)+1):  #자릿수를 뒤에서부터 두자릿씩 끊어서 계산하기에 자릿수에 맞게 반복문을 돌리게 하면 된다. 그래서 입력 받은 값을 string 으로 형변환 한 후, len으로 자릿수를 구했다. 그 후에 2로 나누어 산출된 정수 값만큼 반복문으로 돌리게 했다. 그리고 세자리 수일 때를 대비해 + 1을 더해 반복문이 한번만 더 돌 수 있도록 했다.
    answer += number % 100
    number //= 100

print(answer)