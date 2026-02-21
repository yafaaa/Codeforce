nums = []
n = int(input())
for _ in range(n):
    _, *res = list(map(int, input().split()))
    nums.append(res)
n_split = 0

for i in range(1,n):
    l = nums[i]
    if l[i]<l[i-1]:
        n_split += 1

n_comb = 2*n_split

for i in range(1,len(nums[0])):
    l = nums[0]
    if l[i]<l[i-1]:
        n_split += 1
        n_comb += 1
print(n_split, n_comb)

    


