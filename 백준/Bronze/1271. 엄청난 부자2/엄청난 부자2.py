import sys

# 최백준 조교가 가진 돈 : n
# 생명체의 수 m

n,m = map(int, sys.stdin.readline().split())

print(f'{n//m}\n{n%m}')