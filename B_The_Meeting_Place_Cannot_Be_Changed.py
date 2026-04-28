n = int(input)
s = list(map(int, input().split()))
v = list(map(int, input().split()))
l = min(s)
r = max(s)
def fun(d):
    mn = float('inf')
    for s, v in zip(s,v):
        t = abs(s-d)/v
        mn = min(mn, t)
    