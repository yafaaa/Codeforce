import math
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(key=lambda x: x%2)
    cnt = 0
    for i in range(n):
        if nums[i]%2 == 0:
            cnt += n-(i+1)
        else:
            for j in range(i+1,n):
                if math.gcd(nums[i], nums[j]) > 1:
                    cnt += 1
    print(cnt)
    
