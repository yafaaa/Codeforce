from itertools import accumulate
n = int(input())
nums = list(map(int, input().split()))
s_nums = sorted(nums)
s_prefix= list(accumulate([0]+s_nums))
prefix = list(accumulate([0]+nums))

for _ in range(int(input())):
    op, a, b = map(int, input().split())
    if op == 1:
        print(prefix[b]-prefix[a-1])
    else:
        print(s_prefix[b]-s_prefix[a-1])
