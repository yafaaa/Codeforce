test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    if k> ((n-1)//2):
        print(-1)
        continue
    
    if k == 0:
        l = [i for i in range(1,n+1)]
        print(*l)
        continue
    l = [0]*n
    a = n
    for i in range(k):
        j = 2*i+1
        l[j] = a
        a-=1
    for i in range(n):
        if l[i] == 0:
            l[i] = a
            a-=1  
    print(*l)
