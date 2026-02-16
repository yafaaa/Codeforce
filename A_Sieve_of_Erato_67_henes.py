
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    t = 1
    for num in nums:
        t *= num
        
    if t%67 == 0:
        print("YES")
    else: print("NO")
        



