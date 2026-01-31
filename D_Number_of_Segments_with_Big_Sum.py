n, t = map(int, input().split())
l = list(map(int, input().split()))
a,s,c,b = 0, 0, 0, 0
while b<n:
    s+=l[b]
    while a<n and s>=t:
        s-=l[a]
        a+=1
    c+=(b-a+1)
    b+=1
c=(n*(n+1)//2)-c
print(c)
    
    
