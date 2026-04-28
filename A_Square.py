for _ in range(int(input())):
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1:
        print('YES')
    else:
        print('NO')