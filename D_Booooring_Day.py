
for _ in range(int(input())):
    n , l, r = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    a, b = 0, 0
    curr_s = 0
    for b in range(n):
        curr_s += nums[b]
        if curr_s < l:
            continue
        while a+1<=b and curr_s > r:
            curr_s -= nums[a]
            a += 1
        if l<=curr_s<=r:
            a = b+1
            cnt += 1
            curr_s = 0
        
    print(cnt)