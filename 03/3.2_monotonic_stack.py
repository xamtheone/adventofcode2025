import sys

data = [[int(n) for n in d] for d in open(sys.argv[1]).read().splitlines()]

L = 12
s = 0
for bank in data:
    largest_joltage = [] # monotonic stack
    for i, digit in enumerate(bank):
        while largest_joltage and digit > largest_joltage[-1] and len(largest_joltage) + len(bank) - i > L:
            largest_joltage.pop()

        if len(largest_joltage) < L:
            largest_joltage.append(digit)

    s += sum(n * 10**(L - i - 1) for i, n in enumerate(largest_joltage))
print(s)