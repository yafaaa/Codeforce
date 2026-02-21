n = int(input())
ans = list(map(int, input().split()))
m = max(ans)
if (m*(m+1))//2 != sum(ans):
    print(((m*(m+1))//2)-sum(ans))
else:
    print(m+1)


# f = False
# for i in range(1,n):
#     if ans[i] - ans[i-1] >1:
#         f = True
#         print(ans[i-1]+1)
#         break
# if not f:
#     print(ans[-1]+1)
