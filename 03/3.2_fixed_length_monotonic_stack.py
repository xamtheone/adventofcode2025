import sys

data = [[int(n) for n in d] for d in open(sys.argv[1]).read().splitlines()]

L = 12
s = 0
for bank in data:
    largest_joltage = [0] * L # fixed length monotonic stack
    pointer = -1
    for i, digit in enumerate(bank):
        while pointer >= 0 and digit > largest_joltage[pointer] and pointer + 1 + len(bank) - i > L:
            largest_joltage[pointer] = 0
            pointer -= 1

        if pointer < L - 1:
            pointer += 1
            largest_joltage[pointer] = digit

    s += sum(n * 10**(L - i - 1) for i, n in enumerate(largest_joltage))
print(s)