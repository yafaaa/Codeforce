from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s, t = input().split()
    ds = Counter(s)
    dt = Counter(t)
    if ds == dt:
        print('YES')
    else:
        print('NO')