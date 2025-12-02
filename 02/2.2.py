import sys
import re

data = [[int(n) for n in d.split('-')] for d in open(sys.argv[1]).read().split(',')]
ans = 0
for start, end in data:
    for n in range(start, end + 1):
        s = str(n)
        m = re.match(r'^(.+)\1+$', s)
        if m:
            ans += n
print(ans)