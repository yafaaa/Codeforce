n, t = map(int, input().split())
l = list(map(int, input().split()))
a,s,b = 0, 0, 0
c = 0
while b < n:
    while s+l[b] > t:
        s-=l[a]
        a+=1
    s+=l[b]
    c+=(b-a+1)
    b+=1
    
print(c)
    