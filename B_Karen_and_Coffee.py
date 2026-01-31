mt = 200000
diff = [0] * (mt + 2)
n, k, q = map(int, input().split())

for i in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

for i in range(1, mt + 2):
    diff[i] += diff[i-1] 

prefix = [0] * (mt + 1)
for i in range(1, mt + 1):
    prefix[i] = prefix[i-1] + (1 if diff[i] >= k else 0)

for i in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])