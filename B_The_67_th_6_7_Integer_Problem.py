
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    mx = max(nums)
    sm = sum(nums)
    sm -= mx
    print(-sm+mx)