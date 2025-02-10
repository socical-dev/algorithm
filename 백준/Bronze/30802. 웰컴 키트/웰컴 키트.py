# 첫째줄은 N 명
# 둘째줄은 사이즈별로 티셔츠 주문 수
# 셋째줄은 T = 한 묶음에 갯수, P = 펜 한묶음에 갯수

import sys

input = [v.strip() for v in sys.stdin.readlines()]

N = int(input[0])
clothes_size = list(map(int, input[1].split()))
T = int(input[2].split()[0])
P = int(input[2].split()[1])

order_clothes_set = 0
order_pen = f"{N // P} {N % P}"

for c_s in clothes_size:
    if c_s%T == 0 and c_s != 0:
        if(c_s//T == 0):
            order_clothes_set += 1
        else:
            order_clothes_set += c_s//T
    elif c_s == 0:
        pass
    else:
        order_clothes_set += c_s//T + 1
    
print(f"{order_clothes_set}\n{order_pen}")