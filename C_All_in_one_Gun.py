for _ in range(int(input())):
    n, h, k = map(int, input().split())
    nums = list(map(int, input().split()))
    total = sum(nums)  
    times = h // total
    left = h % total
    cnt = 0
    idx = 0
    if not left:
        print((times*n)+(k*(times-1))+idx)
    else:
        prefix_min = [nums[0]] + [0] * (n-1)
        prefix_max = [nums[n-1]] + [0] * (n-1)
        for i in range(1,n):
            prefix_min[i] = min(prefix_min[i-1], nums[i])
        
        for i in range(n-2, -1, -1):
            prefix_max[i] = max(prefix_max[i+1], nums[i])
        

        for i in range(n):
            cnt += nums[i]
            idx = i+1
            if cnt >= left:
                break
            
            b = prefix_max[i]
            a = prefix_min[i]
            cnt -= a
            cnt += b
            
            if cnt >=left:
                break
            cnt += a
            cnt -= b

        print((times*n)+(k*times)+idx)
    
    
        