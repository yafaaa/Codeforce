n, s = map(int, input().split())
nums = list(map(int, input().split()))
a = 0
curr_s = 0
ans = 0
for b in range(n):
    curr_s += nums[b]
    while curr_s > s:
        curr_s -= nums[a]
        a += 1
    ans += (b-a+1)
print(ans)


























# n, t = map(int, input().split())
# l = list(map(int, input().split()))
# a,s,b = 0, 0, 0
# c = 0
# while b < n:
#     while s+l[b] > t:
#         s-=l[a]
#         a+=1
#     s+=l[b]
#     c+=(b-a+1)
#     b+=1
    
# print(c)
    