from collections import Counter
import math
def fun():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    d = Counter(nums)
    unique = len(d)
    bucket_cap = max(math.ceil(unique/k), math.ceil(n/k))
    if max(d.values()) > k:
        return "NO"
    bucket = [[] for _ in range(k)]
    bucket_set = [set() for _ in range(k)]
    t = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        j = t%k
        if num not in bucket_set[j] and len(bucket[j]) < bucket_cap:
            bucket[j].append(i)
            bucket_set[j].add(num)
            i += 1
        t += 1
    
    
    for i in range(k):
        for idx in bucket[i]:
    
            nums[idx] = i+1
            
    
    return "YES" + '\n' + " ".join(map(str,nums))


     
print(fun())




