import math
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    hour = list(map(int, input().split()))
    l = 1
    r = max(nums)
    ans = -1
    def fun(n):
        cnt = 0
        for i in range(len(nums)):
            num = nums[i]
            cnt += math.ceil(num/n) * hour[i]
        return cnt <= k
    
    while l <= r:
        m = (l+r)//2

        if fun(m):
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)

