for _ in range(int(input())):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    curr_s = 0
    a = 0
    mn = float('inf')
    for b in range(n):
        curr_s += nums[b]
        if curr_s < k*m:
            continue
        while curr_s-nums[a] >= k*m:
            curr_s -= nums[a]
            a += 1 
        mn = min(mn, curr_s)
        curr_s = 0
    if mn == float('inf'):
        print(-1)
    else:
        print(sum(nums)-mn)
        

        

    







    