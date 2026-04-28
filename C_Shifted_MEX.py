for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    mx = 1
    prev = nums[0]
    c = 1
    for i in range(1,n):
        if nums[i]-nums[i-1] == 1:
            c += 1
            mx = max(mx, c)
        elif nums[i]-nums[i-1] < 1:
            pass
        else:
            c = 1
    print(mx) 
        
        



