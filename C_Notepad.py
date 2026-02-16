
for _ in range(int(input())):
    n = int(input())
    string = input()
    cnt = 0
    ans = []
    i = 0
    b = 0
    while i< n:
        cnt += 1
        if string[i]  in ans:
            b = i+1
            while b<n and string[i:b+1] in "".join(ans):
                b += 1 
            if b > i+1:
                cnt = n-1
                break
        ans.append(string[i])
        i = max(i+1,b)  
    if cnt < n:
        print("YES")
    else:
        print("NO")












# for _ in range(int(input())):
#     n = int(input())
#     string = input()
#     d = dict()
#     f = False
#     for i in range(n-1):
#         strr = string[i:i+2]
#         if strr in d:
#             if d[strr] < i-1:
#                 f = True
#                 break
#         else:
#             d[strr] = i

#     if f:
#         print("YES")
#     else:
#         print("NO")















