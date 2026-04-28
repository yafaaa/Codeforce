for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    i = 0
    while i < n-1:
        a = nums[i] % 2
        val = nums[i]
        idx = 0
        for j in range(i+1,n):
            b = nums[j] % 2
            if a!=b and val>nums[j]:
                val = nums[j]
                idx = j
                
        if idx:
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1
    
    print(*nums)
            