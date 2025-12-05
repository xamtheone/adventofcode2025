import sys

dranges, _ = open(sys.argv[1]).read().strip().split('\n\n')

prev = ()
ranges = []
unordered = []
for r in sorted(dranges.splitlines()):
    a, b = r.split('-')
    unordered.append((int(a), int(b)))

for a, b in sorted(unordered, key=lambda r: r[0]):
    if a in prev:
        ranges[-1] = range(prev.start, max(b + 1, prev.stop))
        prev = ranges[-1]
    else:
        rnge = range(a, b+1)
        ranges.append(rnge)
        prev = rnge


print(sum(r.stop - r.start for r in ranges))