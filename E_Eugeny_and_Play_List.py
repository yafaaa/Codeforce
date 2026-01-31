n, m = map(int, input().split())
prefix = [0]
for _ in range(n):
    c, t = map(int, input().split())
    total_time = c * t
    prefix.append(prefix[-1] + total_time)
queries = list(map(int, input().split()))

for v in queries:
    a = 0
    b = n  
    while a < b:
        mid = (a + b) // 2
        if prefix[mid] >= v:
            b = mid
        else:
            a = mid + 1
    print(a)