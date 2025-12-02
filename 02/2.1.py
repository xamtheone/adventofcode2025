import sys

data = [[int(n) for n in d.split('-')] for d in open(sys.argv[1]).read().split(',')]
ans = 0
for start, end in data:
    for n in range(start, end + 1):
        s = str(n)
        if s[:len(s)//2] == s[len(s)//2:]:
            ans += n
print(ans)