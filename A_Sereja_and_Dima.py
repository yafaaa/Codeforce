from collections import deque
n = int(input())
l = deque(map(int, input().split()))
s, d = 0, 0
f = True
while l:
    if l[0]>l[-1]:
        if f:
            s+=l.popleft()
            f = False
        else:
            d+=l.popleft()
            f = True
    else:
        if f:
            s+=l.pop()
            f = False
        else:
            d+=l.pop()
            f = True
print(f"{s} {d}")
