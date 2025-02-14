import sys

input = [n.strip() for n in sys.stdin.readlines()]

n_subjects = int(input[0])
record = [int(n) for n in input[1].split()]
sham_record = [n / max(record) * 100 for n in record]

average = sum(sham_record) / n_subjects

print(average)