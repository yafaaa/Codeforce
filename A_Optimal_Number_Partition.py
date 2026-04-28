n= int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(n//2):
    b = n-1-i
    ans += (nums[i]+nums[b]) ** 2
print(ans)