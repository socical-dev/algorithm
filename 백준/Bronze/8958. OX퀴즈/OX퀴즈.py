import sys

input = sys.stdin.readlines()
return_num = 0

for i in range(1, len(input)):
    strip_input = input[i].strip()
    n = 0
    for v in strip_input:
        if v == 'O':
            n += 1
            return_num += n
        else:
            n = 0
    
    print(return_num)
    return_num = 0