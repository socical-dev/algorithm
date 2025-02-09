# max() + min()
import sys

code = [n.strip() for n in sys.stdin.readlines()]

list_second_code = list(map(int, code[1].split()))
print(f"{min(list_second_code)} {max(list_second_code)}")