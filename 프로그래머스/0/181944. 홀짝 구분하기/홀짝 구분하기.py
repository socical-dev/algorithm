a = int(input())

# a 의 나머지를 구했을 때 1 이상이면, 짝수가 아니기에 다음과 같은 조건식 작성.
if a % 2 != 0 :
    print(f'{a} is odd')
else:
    print(f'{a} is even')