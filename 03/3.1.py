import sys

data = [[int(n) for n in d] for d in open(sys.argv[1]).read().splitlines()]
s = 0
for bank in data:
    left = max(bank[:-1])
    i = bank.index(left)
    right = max(bank[i+1:])
    batteries = left * 10 + right
    s += batteries
print(s)