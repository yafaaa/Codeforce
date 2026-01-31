x, y = map(int, input().split())
lx = list(map(int, input().split()))
ly = list(map(int, input().split()))
a, c = 0, 0
l = []
for b in ly:
    while a<x and lx[a]<b:
        c+=1
        a+=1
    l.append(c)
print(*l)