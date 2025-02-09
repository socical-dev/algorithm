import sys

n_list = [n.strip() for n in sys.stdin.readlines() if int(n.split()[0]) + int(n.split()[1]) != 0]
        
for n in n_list:
    n = list(map(int, n.split()))
    print(n[0] + n[1])