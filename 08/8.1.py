import math
import sys

def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)

def cmp_key(p, q):
    a = sum(p)
    b = sum(q)
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def bfs(junction_boxes, connections):
    visited = set()
    circuits = []
    # Build all circuits with BFS
    for junction_box in junction_boxes:
        if junction_box in visited: continue
        circuit = set()
        visited.add(junction_box)
        Q = [junction_box]
        while Q:
            current = Q.pop(0)
            circuit.add(current)

            if current in connections:
                for next in connections[current]:
                    if next not in visited:
                        visited.add(next)
                        Q.append(next)
        circuits.append(circuit)
    return circuits

junction_boxes = [tuple(map(int, r.split(','))) for r in open(sys.argv[1])]

allcon = {}
connections = {}
indexes = {}
shorts = []
connected = set()
for i, jb1 in enumerate(junction_boxes):
    indexes[jb1] = i
    closest = None
    min_closest = 9999999999
    for jb2 in junction_boxes:
        if jb1 == jb2: continue
        # Filter boxes tat are already directly connected
        if (jb2, jb1) in connected: continue

        dist = distance(jb1, jb2)
        if dist < min_closest:
            min_closest = dist
            closest = jb2

    connected.add((jb1, closest))
    shorts.append((jb1, closest, min_closest))

print(len(shorts))
shorts = sorted(shorts, key=lambda t: t[2])

# for s in shorts:
#     # print(indexes[s[0]], indexes[s[1]], round(s[2], 1))
#     print(s)

sample_size = 1000 if len(junction_boxes) == 1000 else 10

for child, parent, dist in shorts[:sample_size]:
    connections.setdefault(parent, [])
    connections.setdefault(child, [])
    connections[parent].append(child)
    connections[child].append(parent)

circuits = bfs(junction_boxes, connections)

acc = 1
for circuit in sorted(circuits, reverse=True, key=lambda c: len(c))[:3]:
    acc *= len(circuit)
    # print([indexes[jb] for jb in circuit])
    print(circuit)
print(acc)