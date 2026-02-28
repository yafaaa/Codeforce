n, s = map(int, input().split())
nums = list(map(int, input().split()))

l = []
for i in range(n):
    l.append((nums[i], i + 1))

l.sort()

curr_sum = 0
res = []
for num, i in l:
    if curr_sum + num <= s:
        curr_sum += num
        res.append(i)
    else:
        break

print(len(res))
if len(res) > 0:
    print(*(sorted(res)))