str = input()
list = list(str)    # string은 일련의 문자로 이어져있는 시퀀스이기에 list로 문자를 분류를 한다.


for i in range(len(list)):  # list의 길이의 범위 만큼 반복문을 실행하여 문자 한 자씩 출력을 한다.
    print(list[i])
