from collections import defaultdict
n, s = map(int, input().split())
nums = list(map(int, input().split()))
d = defaultdict(list)
for i, num in enumerate(nums):
    d[num].append(i)

nums.sort()
res = []

for num in nums:
    if s < num:
        break
    s -= num
    res.append(str(d[num].pop() + 1))
    
if not res:
    print(0)
else:
    print(len(res))
    print(" ".join(res))
    

























# l = []
# for i in range(n):
#     l.append((nums[i], i + 1))

# l.sort()

# curr_sum = 0
# res = []
# for num, i in l:
#     if curr_sum + num <= s:
#         curr_sum += num
#         res.append(i)
#     else:
#         break

# print(len(res))
# if len(res) > 0:
#     print(*(sorted(res)))