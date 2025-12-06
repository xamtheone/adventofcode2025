import sys
import re

data = open(sys.argv[1]).read().splitlines()
ops = re.sub(r' +', ' ', data.pop()).strip().split(' ')

D = []
i = 0
idx_col = 0
while i < len(data[0]):
    l = 1
    for j in range(len(data)):
        m = re.search(r'\d+', data[j][i:])
        if m:
            l = max(len(m.group()), l)
    D.append([])
    for y in range(len(data)):
        num = data[y][i:i+l]
        D[-1].append(num)

    i += l + 1
    idx_col += 1

s = 0

for idx_col, numbers in enumerate(D):
    group = []
    l = max([len(n) for n in numbers])
    for i in range(len(numbers[0]) - 1, -1, -1):
        acc = ''
        for n in numbers:
            acc += n[i]
        group.append(int(acc)) # Python doesn't care about spaces in numbers for conversion

    if ops[idx_col] == '+':
        s += sum(group)
    else:
        c = 1
        for v in group: c *=v
        s += c
print(s)