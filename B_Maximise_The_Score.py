for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    total = 0
    for i in range(0,n*2,2):
        total += nums[i]
    print(total)
    