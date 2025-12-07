import sys

DP = {}
def dfs(data, xpos, ypos = 0):
    if (xpos, ypos) in DP:
        return DP[(xpos, ypos)]

    c = 0
    for y, r in enumerate(data[ypos:]):
        if r[xpos] == '^':
            c += 1
            if xpos > 0:
                c += dfs(data, xpos - 1, ypos + y + 1)
            if xpos < len(r) - 1:
                c += dfs(data, xpos + 1, ypos + y + 1)
            break
    DP[(xpos, ypos)] = c

    return c

data = [[c for c in r] for r in open(sys.argv[1]).read().strip().splitlines()]

print(dfs(data, len(data[0]) // 2) + 1)