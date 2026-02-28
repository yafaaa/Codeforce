n, s = map(int, input().split())
nums = list(map(int, input().split()))

a, curr_s, ans = 0, 0, 0

for b in range(n):
    curr_s += nums[b]
    while curr_s > s:
        curr_s -= nums[a]
        a += 1
    res = b-a+1
    ans += (res * (res+1))//2
print(ans)