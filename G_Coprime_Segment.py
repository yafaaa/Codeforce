from math import gcd
from functools import reduce
n = int(input())
l = list(map(int, input().split()))
a,m, g = 0, 0, 0
for b in range(n):
    g = reduce(gcd, l[a:b+1])
    while gcd(*l[a:b+1])!=1:
        a+=1
        g = reduce(gcd, l[a:b+1])
    m = min(m, b-a+1)
print(m)
