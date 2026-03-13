n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefix = 0
costs = []

for i in range(n - 1):
    prefix += 1 if not nums[i] % 2 else -1

    if prefix == 0:
        costs.append(abs(nums[i] - nums[i+1]))

costs.sort()

cnt = 0
for c in costs:
    if k < c:
        break
    k -= c
    cnt += 1

print(cnt)