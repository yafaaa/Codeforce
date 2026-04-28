
for _ in range(int(input())):
    n, h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        cnt += max(list(map(int, input().split())))
    if cnt >= h:
        print('YES')
    else:
        print('NO')