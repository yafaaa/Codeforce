from collections import deque
nums = []
n = int(input())
for _ in range(n):
    nums.append(list(map(int, input().split())))

nums.sort(key=lambda x: x[1])

left = 0
k = 0
cost = 0
right = n-1
while right > -1:
    a = nums[left]
    b = nums[right]

    while b[0] and a[1]> k:
        b[0] -= 1
        cost += 2
        k += 1
    if not b[0] and right > left:
        right -= 1
    while a[1]<=k:
        cost += a[0]
        if left+1 < n:
            left += 1
            a = nums[left]
        else:
            break
    
    
print(cost)


        