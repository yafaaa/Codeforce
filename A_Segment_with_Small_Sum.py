n, t = map(int, input().split())
l = list(map(int, input().split()))
a, s = 0, 0
m = float('-inf')
for b in range(n):
    while s+l[b]> t:
        s-=l[a]
        a+=1
    m = max(m, b-a+1)
    s+=l[b]
print(m)