n, s = map(int, input().split())
nums = list(map(int, input().split()))
a, curr_s = 0, 0
mn = float('inf')

for b in range(n):
    curr_s += nums[b]
    if curr_s < s:
        continue
    while curr_s >= s:
        mn = min(mn, b-a+1)
        curr_s -= nums[a]
        a += 1
print(mn if mn != float('inf') else -1)




























# n, t = map(int, input().split())
# l = list(map(int, input().split()))
# a,s= 0, 0
# m = float('inf')
# for b in range(n):
#     s+=l[b]
#     while s-l[a]>=t:
#         s-=l[a]
#         a+=1
#     if s>=t:
#         m = min(m, b-a+1)
# print(m if m != float('inf') else -1)
    