n, t = map(int, input().split())
l = list(map(int, input().split()))
a,c  = 0, 0
d = dict()
for b in range(n):
    d[l[b]] =d.get(l[b],0) + 1
    while len(d)>t:
        d[l[a]]-=1
        if d[l[a]]==0:
            del d[l[a]]
        a+=1
    c+=(b-a+1)
print(c)

    

