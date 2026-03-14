for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    p = [0] * n
    f = True
    i = 0
    
    while i < n:
        j = i
        
        while j < n - 1 and nums[j + 1] == nums[i]:
            j += 1
        
        if i == j:
            f = False
            break

        for k in range(i, j):
            p[k] = k + 2
        p[j] = i + 1
        
        i = j + 1
        
    if f:
        print(" ".join(map(str,p)))
    else:
        print(-1)