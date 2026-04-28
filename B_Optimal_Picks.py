
for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    eve = 0
    noah = 0
    t_noah = 0
    for i in range(1,n,2):
        a = nums[i-1]
        b = nums[i]
        noah += b
        if k:
            d = a-b
            t =  min(k, d)
            t_noah += t
            k -= t

    eve = sum(nums)-noah
    print(eve - noah-t_noah)
    


