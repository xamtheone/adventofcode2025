import math
import sys

def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)

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
        shorts.append((jb1, jb2, dist))
        connected.add((jb1, jb2))

shorts = sorted(shorts, key=lambda t: t[2])

for child, parent, dist in shorts:
    connections.setdefault(parent, [])
    connections.setdefault(child, [])
    connections[parent].append(child)
    connections[child].append(parent)
    
    circuits = bfs(junction_boxes, connections)
    if len(circuits) == 1:
        print(child[0] * parent[0])
        break