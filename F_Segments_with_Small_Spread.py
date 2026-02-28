# from collections import defaultdict
# n, k = map(int, input().split())
# nums = list(map(int, input().split()))
# d = defaultdict(int)
# a = 0
# ans = 0
# for b in range(n):
#     d[nums[b]] += 1
#     mx = max(d.keys())
#     mn = min(d.keys())
#     while mx-mn > k:
#         d[nums[a]] -= 1
#         if not d[nums[a]]:
#             del d[nums[a]]
#             if nums[a] == mx:
#                 mx = max(d.keys())
#             elif nums[b] == mx:
#                 mn = min(d.keys())
#         a += 1
#     ans += b-a+1
# print(ans)


























# # from collections import deque
# # mindq=deque()
# # maxdq=deque()
# # n, t = map(int, input().split())
# # l = list(map(int, input().split()))
# # a,s,c = 0,0,0
# # for b in range(n):
# #     while mindq and mindq[-1]>l[b]:
# #         mindq.pop()
# #     mindq.append(l[b])
# #     while maxdq and maxdq[-1]<l[b]:
# #         maxdq.pop()
# #     maxdq.append(l[b])
# #     while (maxdq[0]-mindq[0])>t:
# #         if l[a] == maxdq[0]:
# #             maxdq.popleft()
# #         if l[a] == mindq[0]:
# #             mindq.popleft()
# #         a+=1
# #     c+=(b-a+1)
# # print(c)


    
