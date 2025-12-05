import sys

dranges, ids = open(sys.argv[1]).read().strip().split('\n\n')

ranges = []
for r in dranges.splitlines():
    a, b = r.split('-')
    ranges.append(range(int(a), int(b)+1))

ids = [int(n) for n in ids.splitlines()]

count_fresh = 0
for id in ids:
    for r in ranges:
        if id in r:
            count_fresh += 1
            break
print(count_fresh)