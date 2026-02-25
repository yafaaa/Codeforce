
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    prev = 1 if nums[0] > 0 else -1
    s = 0
    p = nums[0]
    for i in range(1,n):
        curr = 1 if nums[i] > 0 else -1
        if curr != prev:
            s += p
            p = nums[i]
            prev *= -1

        else:
            p = max(p,nums[i])
    s += p
    print(s)