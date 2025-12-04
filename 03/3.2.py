import sys

data = [[int(n) for n in d] for d in open(sys.argv[1]).read().splitlines()]
s = 0
for bank in data:
    batteries = 0
    start = 0
    for i in range(12):
        left = 0
        index = 0
        for j in range(start, len(bank) - (12-i)+1):
            if bank[j] > left:
                left = bank[j]
                index = j
        start = index + 1
        batteries += left * 10**(11-i)
    s += batteries
print(s)