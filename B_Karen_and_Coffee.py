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

# n, k, q = map(int, input().split())
# t = 200001
# diff = [0] * t

# for _ in range(n):
#     l, r = map(int, input().split())
#     diff[l] += 1
#     if r+1 < t:
#         diff[r+1] -= 1

# for i in range(1,t):
#     diff[i] = diff[i-1] + diff[i]

# for i in range(1,t):
#     diff[i] = 1 if diff[i] >=k else 0

# for i in range(1,t):
#     diff[i] +=  diff[i-1]

# for _ in range(q):
#     l, r = map(int, input().split())
#     print(diff[r]-diff[l-1])