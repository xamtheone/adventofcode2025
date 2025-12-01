import sys

data = open(sys.argv[1]).read().splitlines()

pos = 50
s = 0
for i in data:
    d = i[0]
    v = int(i[1:])
    if d == 'R':
        for _ in range(v):
            pos += 1
            if pos % 100 == 0:
                s += 1
    else:
        for _ in range(v):
            pos -= 1
            if pos % 100 == 0:
                s += 1
print(s)