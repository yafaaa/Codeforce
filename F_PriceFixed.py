import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

nums.sort(key=lambda x: x[1])

left = 0
right = n - 1
k = 0
cost = 0

while left <= right:
    if k >= nums[left][1]:
        
        cost += nums[left][0]
        k += nums[left][0]        
        left += 1
    else:
        
        batch = min(nums[right][0], nums[left][1] - k)  
        cost += 2 * batch
        k += batch
        nums[right][0] -= batch
        if nums[right][0] == 0:
            right -= 1
        

print(cost)