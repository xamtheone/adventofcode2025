import sys

grid = open(sys.argv[1]).read().splitlines()

G = len(grid)

dirs = (
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
)
s= 0
for y in range(G):
    for x in range(G):
        if grid[y][x] != '@': continue
        c = 0
        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < G and 0 <= yy < G and grid[yy][xx] == '@':
                c += 1
        if c < 4:
            s += 1
print(s)