from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    d = defaultdict(int)
    a = 0
    mx = 0
    for b in range(n):
        
        if b-1 > -1 and  nums[b]-nums[b-1] > 1:
                a = b
                d = defaultdict(int)
                d[nums[b]] += 1
                continue

        
        while len(d.keys())>k:
            d[nums[a]] -= 1
            if not d[nums[a]]:
                del d[nums[a]]
            a +=1
        mx = max(mx, b-a+1)
    print(mx)