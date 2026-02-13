
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    d = dict()
    l = []
    for num in nums:
        if num%k == 0:
            pass
        else:
            l.append(k-num%k)
    maxx = 0

    for num in l:
        
        if num not in d:
            maxx = max(maxx, num+1)
            d[num] = 1
        else:
            temp = ((d[num])*k) + num 
            maxx = max(maxx, temp+1)
            d[num] += 1
    print(maxx)