
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    strt_pt = [nums[0]]

    for num in nums[1:]:
        if strt_pt[-1] != num:
            strt_pt.append(num)
            
    a = 0
    mx = 0
    for b in range(len(strt_pt)):    

        while strt_pt[b] - strt_pt[a] > n-1:
            a += 1
        mx = max(mx, b-a+1)

    print(mx)



    

        
        
