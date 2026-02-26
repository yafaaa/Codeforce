import math
for _ in range(int(input())):
    n, m, d = map(int,(input().split()))
    num = (d//m) + 1
    print(math.ceil(n/num))