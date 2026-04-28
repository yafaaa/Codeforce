
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    # print(nums)
    def mex(arr):
        seen = set(arr)
        
        for i in range(len(arr)):
            if i not in seen:
                return i
        
        return len(arr)
    ans = []
    while nums != sorted(nums):
        t = mex(nums)
        if t == n:
            for i in range(n):
                if nums[i] != i:
                    nums[i] = t
                    ans.append(i)
                    break
        else:
            nums[t] = t
            ans.append(t)
        

                
    print(nums)
    # print(len(ans))
    # print(*ans)
    
        