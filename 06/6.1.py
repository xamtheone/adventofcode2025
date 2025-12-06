import sys
import re

data = open(sys.argv[1]).read().strip()
data = [r.strip().split(' ') for r in re.sub(r' +', ' ', data).splitlines()]

D = {}
s = 0
for r in data:
    for i, n in enumerate(r):
        if n not in ('*', '+'):
            D[i] = D.setdefault(i, [])
            D[i].append(int(n))
        else:
            if n == '+':
                s += sum(D[i])
            else:
                c = 1
                for v in D[i]:
                    c *=v
                s += c 
print(s)
