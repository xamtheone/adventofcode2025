import sys

data = [r.split() for r in open(sys.argv[1])]

s = 0

for line in data:
    line.pop()
    end_state = tuple([c == '#' for c in line.pop(0)[1:-1]])
    buttons = [list(map(int, n[1:-1].split(','))) for n in line]

    lights = tuple([False] * len(end_state))
    visited = set([tuple(lights)])
    Q = [(lights, 0)]

    count = 0
    # BFS
    while Q:
        lights, count = Q.pop(0)

        if lights == end_state:
            break

        for button in buttons:
            new_lights = list(lights)
            for light_offset in button:
                new_lights[light_offset] = not new_lights[light_offset]
            new_lights = tuple(new_lights)
            if new_lights not in visited:
                visited.add(new_lights)
                Q.append((new_lights, count + 1))

    s += count
print(s)