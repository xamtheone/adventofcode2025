import sys

def are_corners_in_four_walls(minx, miny, maxx, maxy, horizontals, verticals):
    valid_corners = 0
    for px, py in ((minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)):
        hitup = False
        hitdown = False
        hitleft = False
        hitright = False

        for (sx, sy), (ex, ey) in horizontals:
            inside = min(sx, ex) <= px <= max(sx, ex)
            if not hitup and sy <= py and inside:
                hitup = True
                if hitdown: break
            if not hitdown and sy >= py and inside:
                hitdown = True
                if hitup: break
        
        if hitup and hitdown:
            for (sx, sy), (ex, ey) in verticals:
                inside = min(sy, ey) <= py <= max(sy, ey)
                if not hitleft and sx <= px and inside:
                    hitleft = True
                    if hitright: break
                if not hitright and sx >= px and inside:
                    hitright = True
                    if hitleft: break

        if hitup and hitleft and hitdown and hitright:
            valid_corners += 1
    
    return valid_corners == 4

def is_valid_middle_vert_axis(miny, maxy, xmid, horizontals):
    for (sx, sy), (ex, ey) in horizontals:
        if miny < sy < maxy and min(sx, ex) <= xmid <= max(sx, ex):
            return False
    return True

coords = [list(map(int, r.split(','))) for r in open(sys.argv[1])]
coords.append(coords[0])

vertices = []
horizontals = []
verticals = []

for i in range(len(coords) - 1):
    vertices.append((coords[i], coords[i+1]))
    if coords[i][0] == coords[i+1][0]:
        verticals.append((coords[i], coords[i+1]))
    else:
        horizontals.append((coords[i], coords[i+1]))

best_area = 0
best = (0, 0, 0, 0)
for x, y in coords:
    for xx, yy in coords:
        area = (1 + abs(x - xx)) * (1 + abs(y - yy))
        if area <= best_area: continue

        minx = min(x, xx)
        maxx = max(x, xx)
        miny = min(y, yy)
        maxy = max(y, yy)
        xmid = min(x, xx) + abs(x - xx) // 2

        if not is_valid_middle_vert_axis(miny, maxy, xmid, horizontals): continue
        if not are_corners_in_four_walls(minx, miny, maxx, maxy, horizontals, verticals): continue

        # check intersecting horizontals on the two vertical sides
        skip = False
        for (sx, sy), (ex, ey) in horizontals:
            if maxy > sy > miny and (min(sx, ex) < minx < max(sx, ex) or min(sx, ex) < maxx < max(sx, ex)):
                skip = True
                break
        if skip: continue

        best_area = area
        best = (x, y, xx, yy)

print(best_area)