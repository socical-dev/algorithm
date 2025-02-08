# 두 정수 시:H, 분:M
# H : M 보다 45분 일찍 기상
# 600 + 10 = 610 - 45 -> 565
# 565 // 60 = 9  565 % 60 = 25

import sys

H, M = map(int, sys.stdin.readline().split())

before_45_m = (H*60 + M) - 45

if H == 0 and (H*60 + M) - 45 < 0:
    before_45_m = (24*60 + M) - 45

print (before_45_m // 60, before_45_m % 60)