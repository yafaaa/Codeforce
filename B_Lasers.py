
for _ in range(int(input())):
    n, m , x, y = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    cnt = 0
    
    for i in range(n):
        if l1[i] <= y:
            cnt += 1
        else:
            break
    for i in range(m):
        if l2[i] <= x:
            cnt += 1
        else:
            break
    print(cnt)