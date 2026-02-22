from collections import Counter
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input()))
    d = Counter(nums)
    if 0 in d and d[0] == 1: