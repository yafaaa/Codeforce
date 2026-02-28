
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    m = max(nums)
    print(nums.count(m))



