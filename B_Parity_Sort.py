
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums_sorted = sorted(nums)
    f = False
    for i in range(n):
        if (nums[i]+nums_sorted[i]) %2 != 0:
            f = True
            print("NO")
            break
    
    if not f:
        print("YES")
