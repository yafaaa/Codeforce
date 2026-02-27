n , m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
a, b = 0, 0
ans = 0
while a<n and b<m:

    if l1[a] == l2[b]:
        ca, cb = 1, 1
        while a+1<n and l1[a] == l1[a+1]:
            ca += 1
            a += 1

        while b+1<m and l2[b] == l2[b+1]:
            cb += 1
            b += 1
        a += 1
        ans += (ca*cb)

    elif l1[a] > l2[b]:
        b += 1

    else:
        a += 1
print(ans)
























# n, m = map(int, input().split())
# ln = list(map(int, input().split()))
# lm = list(map(int, input().split()))
# a, b = 0, 0
# cnt = 0

# while a<n and b<m:
#     if ln[a] == lm[b]:
#         ca, cb = 0, 0
#         val = lm[b]
#         while a<n and ln[a] == val:
#             ca += 1
#             a += 1
#         while b<m and lm[b] == val:
#             cb += 1
#             b += 1
#         cnt += ca*cb
#     elif ln[a] > lm[b]:
#         b += 1
#     else:
#         a += 1
# print(cnt)
    















# # x, y = map(int, input().split())
# # lx = list(map(int, input().split()))
# # ly = list(map(int, input().split()))
# # a,b = 0, 0
# # s = 0

# # while a<x and b < y:
# #     if lx[a] == ly[b]:
# #         ca, cb = 0, 0
# #         val = ly[b]
# #         while a<x and lx[a] == val:
# #             a+=1
# #             ca+=1
# #         while b<y and ly[b] == val:
# #             b+=1
# #             cb+=1
# #         s+=ca*cb
# #     elif lx[a]<ly[b]:
# #         a+=1
# #     else:
# #         b+=1
    
# # print(s)

