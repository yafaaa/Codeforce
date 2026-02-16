
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    f = True
    for i in range(n):
        a = i+1
        if nums[i]>a and nums[i]%(a*2) != 0:
            f = False
            print("NO")
            break
        elif a>nums[i] and a%nums[i] != 0:
            
            f = False
            print("NO")
            break
    if f:
        print("YES")
    