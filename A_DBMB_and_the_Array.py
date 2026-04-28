
for _ in range(int(input())):
    n, s, x = map(int, input().split())
    nums = list(map(int, input().split()))
    sm = sum(nums)
    if sm > s:
        print('NO')
    else:
        r = sm-s
        if not r % x:
            print('YES')
        else:
            print('NO')