t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    e=sorted(l, reverse=True)
    m1, m2 = e[0], e[1]
    if ((m1 in l[:2] and m2 in l[:2]) or (m1 in l[2:] and m2 in l[2:])):
        print("NO")
    else:
        print("YES")

