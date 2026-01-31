n = int(input())
l = list(map(int, input().split()))
sl = sorted(l)
for i in range(1,len(l)):
    l[i]+=l[i-1]

for i in range(1,len(sl)):
    sl[i]+=sl[i-1]
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == 1:
        if b == 1:
            print(l[c-1])
        else:
            print(l[c-1] - l[b-2])
    else:
        if b == 1:
            print(sl[c-1])
        else:
            print(sl[c-1] - sl[b-2])