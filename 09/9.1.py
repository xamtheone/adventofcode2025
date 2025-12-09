import sys

coords = [list(map(int, r.split(','))) for r in open(sys.argv[1])]

best_area = 0
for x, y in coords:
    for xx, yy in coords:
        area = (1 + abs(x - xx)) * (1 + abs(y - yy))
        if area > best_area:
            best_area = area

print(best_area)