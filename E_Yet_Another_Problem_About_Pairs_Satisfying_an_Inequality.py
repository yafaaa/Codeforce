for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    valid_pair = []
    prefix = [0] * (n+1)
    cnt = 0
    for i in range(n):
        prefix[i+1] = prefix[i]
        if i+1 > nums[i]:
            cnt += prefix[max(0,nums[i]-1)]
            prefix[i+1] += 1

            
    print(cnt)
