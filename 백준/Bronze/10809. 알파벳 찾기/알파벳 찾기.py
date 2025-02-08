# 알파벳이 있다면 알파벳 위치를 없다면 -1을 출력한다.

import sys

S = sys.stdin.readline()
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

filter_s = ""
for a in alph:
    if a in S:
        filter_s += f"{S.index(a)} "
    else:
        filter_s += "-1 "
        
print(filter_s.strip())