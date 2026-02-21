
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    f = False
    for i in range(1,n):
        if abs(nums[i]-nums[i-1]) > 1:
            f = True
            print("NO")
            break
    if not f:
        print("YES")