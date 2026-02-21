
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
b = max(nums[0])
f = False
for i in range(1,n):
    mi = min(nums[i][0],nums[i][1])
    ma = max(nums[i][0],nums[i][1])
    if ma <= b:
        b = ma
    elif mi <= b:
        b = mi
    else:
        f = True
        print("NO")
        break
if not f:
    print("YES")
        


