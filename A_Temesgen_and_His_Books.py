for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    mx = max(nums)
    idx = nums.index(mx)
    if idx == n-1:
        print(mx + max(nums[:-1]))
    else:
        print(mx + nums.pop())