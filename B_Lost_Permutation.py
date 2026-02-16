
for _ in range(int(input())):
    n , s = list(map(int, input().split()))
    arr = list(map(int,input().split()))
    m = max(arr)
    left_from = (m*(m+1)//2)-sum(arr)
    if left_from>s:
        print("NO")
        continue
    
    s -= left_from
    m += 1
    while m <= s:
        s -= m
        m += 1
    if s == 0:
        print("YES")
    else:
        print("NO")


