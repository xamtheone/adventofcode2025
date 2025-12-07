import sys

data = [[c for c in r] for r in open(sys.argv[1]).read().strip().splitlines()]

beams = [0] * len(data[0])
beams[len(data[0]) // 2] = 1

for r in data:
    for i, x in enumerate(r):
        if x == '^' and beams[i] > 0:
            if i > 0:
                beams[i - 1] += beams[i]
            if i < len(r) - 1:
                beams[i + 1] += beams[i]
            beams[i] = 0
print(sum(beams))