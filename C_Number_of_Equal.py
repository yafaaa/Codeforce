x, y = map(int, input().split())
lx = list(map(int, input().split()))
ly = list(map(int, input().split()))
a,b = 0, 0
s = 0

while a<x and b < y:
    if lx[a] == ly[b]:
        ca, cb = 0, 0
        val = ly[b]
        while a<x and lx[a] == val:
            a+=1
            ca+=1
        while b<y and ly[b] == val:
            b+=1
            cb+=1
        s+=ca*cb
    elif lx[a]<ly[b]:
        a+=1
    else:
        b+=1
    
print(s)

