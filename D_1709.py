from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    d1 = {num: i for i, num in enumerate(l1)}
    d2 = {num: i for i, num in enumerate(l2)}
    res = []
    for idx1 in range(n):
        val1 = idx1+1
        if val1 == l1[idx1]:
            continue
        if val1 not in d1:
            if l2[idx1] != val1: 
                idx2 = d2[val1]
                l2[idx1], l2[idx2] = l2[idx2], l2[idx1]
                d2[l2[idx1]], d2[l2[idx2]] = idx1, idx2
                for i in range(idx2-1, idx1-1, -1):
                    res.append([2, i])
            
            l1[idx1], l2[idx1] = l2[idx1], l1[idx1]
            d1[l1[idx1]] = idx1
            d2[l2[idx1]] = idx1
            del d1[l2[idx1]]
            del d2[l1[idx1]] 
            res.append([3, idx1])
        else:
            idx2 = d1[val1]
            l1[idx1], l1[idx2] = l1[idx2], l1[idx1]
            d1[l1[idx1]], d1[l1[idx2]] = d1[l1[idx2]], d1[l1[idx1]]
            for i in range(idx2-1, idx1-1, -1):
                res.append([1, i])
    
    for idx1 in range(n):
        val2 = n + idx1
        if l2[idx1] != val2:
            idx2 = d2[val2]
            l2[idx1], l2[d2[val2]] = l2[d2[val2]], l2[idx1]
            d2[l2[idx1]], d2[l2[d2[val2]]] = d2[l2[d2[val2]]], d2[l2[idx1]]
            t = d2[val2]
            for i in range(idx2-1, idx1-1, -1):
                res.append([2, i])

    print(len(res))
    for l in res:
        print(" ".join(map(str,l)))




