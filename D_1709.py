from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    d1 = {num: i for i, num in enumerate(l1)}
    d2 = {num: i for i, num in enumerate(l2)}

    for idx1 in range(n):
        val1 = idx1+1
        if val1 not in d1:
            if l2[idx1] != val1: 
                idx2 = d2[val1]
                l2[idx1], l2[idx2] = l2[idx2], l2[idx1]
                d2[l2[idx1]], d2[l2[idx2]] = idx1, idx2
                
            
            l1[idx1], l2[idx1] = l2[idx1], l1[idx1]
            d1[l1[idx1]] = idx1
            d2[l2[idx1]] = idx1
            del d1[l2[idx1]]
            del d2[l1[idx1]] 
            
        else:
            idx2 = d1[val1]
            l1[idx1], l1[idx2] = l1[idx2], l1[idx1]
            d1[l1[idx1]], d1[l1[idx2]] = d1[l1[idx2]], d1[l1[idx1]]




