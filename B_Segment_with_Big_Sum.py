n, t = map(int, input().split())
l = list(map(int, input().split()))
a,s= 0, 0
m = float('inf')
for b in range(n):
    s+=l[b]
    while s-l[a]>=t:
        s-=l[a]
        a+=1
    if s>=t:
        m = min(m, b-a+1)
print(m if m != float('inf') else -1)
    