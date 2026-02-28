n, r = map(int, input().split())
nums = list(map(int, input().split()))

a = b = 0
cnt = 0
for a in range(n):
    while b<n and nums[b]-nums[a] <= r:
        b += 1
    cnt += n-b
print(cnt)

