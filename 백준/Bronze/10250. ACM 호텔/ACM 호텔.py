import sys

input = sys.stdin.readlines()
for n_line in input:
    split_n = n_line.strip().split()
    if(len(split_n) == 3):
        user_room = 0
        
        H = int(split_n[0])
        W = int(split_n[1])
        N = int(split_n[2])
        
        if H >= N:
            user_room += N * 100
        elif N % H == 0:
            user_room += H * 100
        else:
            user_room += N % H * 100
            
        if N % H > 0:
            user_room += N // H + 1
        else:
            user_room += N // H
    
        print(user_room)