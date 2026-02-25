nums = []
l_sorted = []
n = int(input())
for _ in range(n):
    _, *res = list(map(int, input().split()))
    nums.append(res)
    l_sorted.extend(res)
l_sorted.sort()
d = {num: i for i, num in enumerate(l_sorted)}
# print(l_sorted)
separate = 0
for l in nums:
    for i in range(len(l)-1):
        idx_in_dict = d[l[i]] 
        if idx_in_dict+1 >= len(l_sorted) or l_sorted[idx_in_dict+1] != l[i+1]:
            separate += 1
com = n+separate-1
print(separate, com)




    


