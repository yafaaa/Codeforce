from collections import deque
mindq=deque()
maxdq=deque()
n, t = map(int, input().split())
l = list(map(int, input().split()))
a,s,c = 0,0,0
for b in range(n):
    while mindq and mindq[-1]>l[b]:
        mindq.pop()
    mindq.append(l[b])
    while maxdq and maxdq[-1]<l[b]:
        maxdq.pop()
    maxdq.append(l[b])
    while (maxdq[0]-mindq[0])>t:
        if l[a] == maxdq[0]:
            maxdq.popleft()
        if l[a] == mindq[0]:
            mindq.popleft()
        a+=1
    c+=(b-a+1)
print(c)


    
