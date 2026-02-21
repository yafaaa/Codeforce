from collections import Counter
for _ in range(int(input())):
    n , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    d = Counter(nums)
    com_list = []
    a, b = 0, 0
    for i in range(n):
        if k - nums[i] not in d:
            com_list.append(nums[i])
            d[nums[i]] -= 1
            if d[nums[i]] == 0:
                del d[nums[i]]
    com_len = len(com_list)
    # print (com_len)
    # continue
    if com_len%2 == 0:
        a += com_len//2
        b += n//2 - a
    else:
        a += com_len//2 + 1
        b += n//2 - a
    print(a, b)
    
    # if a>=b:
    #     print(0)
    # else:
    #     print(b-a)

