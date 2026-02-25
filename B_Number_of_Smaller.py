n, m = map(int, input().split())
ln = list(map(int, input().split()))
lm = list(map(int, input().split()))
a = 0
res = []
for b in range(m):

    while a<n and ln[a]<lm[b]:
        a += 1
    res.append(str(a))
print(" ".join(res))











